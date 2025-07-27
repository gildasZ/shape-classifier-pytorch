
# ShapeClassifier/utils/data_generator.pyimport os
import random
import math
import os
import shutil
from PIL import Image, ImageDraw
import numpy as np

# --- Configuration Constants ---

# 1. Image Specifications
IMG_SIZE = 64
GRAYSCALE_LEVELS = 255
DARK_RANGE = (20, 80)
LIGHT_RANGE = (180, 240)

# 2. Shape Specifications
SHAPES = ['circle', 'square', 'triangle']
CONDITIONS = [
    'fixed_size_fixed_rot',
    'fixed_size_random_rot',
    'random_size_fixed_rot',
    'random_size_random_rot',
]
FIXED_SHAPE_SIZE = 16  # Characteristic length (e.g., radius)
RANDOM_SHAPE_SIZE_RANGE = (12, 21)

# 3. Noise Specifications
NOISE_MEAN = 0
NOISE_STD_DEV = 15

# 4. Dataset Structure
TOTAL_IMAGES = 6000 # Use a smaller number like 60 for quick testing
SPLIT_RATIOS = {'train': 0.7, 'validation': 0.15, 'test': 0.15}


def _apply_gaussian_noise(image: Image.Image) -> Image.Image:
    """
    Applies Gaussian noise to a PIL image.

    Args:
        image: The input PIL image.

    Returns:
        A new PIL image with noise applied.
    """
    img_array = np.array(image, dtype=np.float32)
    noise = np.random.normal(NOISE_MEAN, NOISE_STD_DEV, img_array.shape)
    noisy_img_array = img_array + noise
    # Clip values to be in the valid [0, 255] range
    noisy_img_array = np.clip(noisy_img_array, 0, GRAYSCALE_LEVELS)
    return Image.fromarray(noisy_img_array.astype(np.uint8))


def _draw_shape(draw: ImageDraw.ImageDraw, shape_type: str, center: tuple, size: int, rotation: float, color: int):
    """
    Dispatches to the correct drawing function based on shape_type.
    This function calculates vertices and calls the underlying PIL drawing methods.
    """
    if shape_type == 'circle':
        # For a circle, size is the radius. Bounding box is [x0, y0, x1, y1]
        bbox = [center[0] - size, center[1] - size, center[0] + size, center[1] + size]
        draw.ellipse(bbox, fill=color)
        return

    # For polygons (square, triangle), we define vertices and then rotate/translate them.
    vertices = []
    if shape_type == 'square':
        # For a square, size is half the side length.
        half_size = size
        vertices = [
            (-half_size, -half_size), (half_size, -half_size),
            (half_size, half_size), (-half_size, half_size)
        ]
    elif shape_type == 'triangle':
        # For an equilateral triangle, size is the distance from center to vertex (radius of circumcircle).
        # Vertices are calculated using trigonometry for an equilateral triangle.
        h = size * 3 / 2  # Height relation to circumradius
        side_half = size * math.sqrt(3) / 2
        vertices = [
            (0, -size),
            (-side_half, size / 2),
            (side_half, size / 2)
        ]

    # Rotate vertices if rotation is not 0
    if rotation != 0:
        angle_rad = math.radians(rotation)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        rotated_vertices = []
        for x, y in vertices:
            x_rot = x * cos_a - y * sin_a
            y_rot = x * sin_a + y * cos_a
            rotated_vertices.append((x_rot, y_rot))
        vertices = rotated_vertices

    # Translate vertices to the final center position
    final_vertices = [(v[0] + center[0], v[1] + center[1]) for v in vertices]
    draw.polygon(final_vertices, fill=color)


def _create_and_save_image(output_path: str, shape_type: str, condition: str):
    """
    Creates a single image with one shape and saves it to the specified path.
    This function orchestrates the entire process for one image.
    """
    # 1. Determine background and shape colors with guaranteed contrast
    if random.random() < 0.5:
        bg_color = random.randint(*DARK_RANGE)
        shape_color = random.randint(*LIGHT_RANGE)
    else:
        bg_color = random.randint(*LIGHT_RANGE)
        shape_color = random.randint(*DARK_RANGE)

    image = Image.new('L', (IMG_SIZE, IMG_SIZE), color=bg_color)
    draw = ImageDraw.Draw(image)

    # 2. Determine shape properties based on the condition
    if 'fixed_size' in condition:
        size = FIXED_SHAPE_SIZE
    else:  # random_size
        size = random.randint(*RANDOM_SHAPE_SIZE_RANGE)

    if 'fixed_rot' in condition:
        rotation = 0
    else:  # random_rot
        rotation = random.uniform(0, 360)

    # 3. Safe Placement Calculation
    # We define the margin based on the shape's size to ensure it's fully visible.
    # We use size * 1.5 as a generous margin to account for rotation of all shapes.
    margin = int(size * 1.5)
    center_x = random.randint(margin, IMG_SIZE - margin)
    center_y = random.randint(margin, IMG_SIZE - margin)

    # 4. Draw the shape onto the clean background
    _draw_shape(draw, shape_type, (center_x, center_y), size, rotation, shape_color)
    
    # 5. Apply noise to the entire image
    final_image = _apply_gaussian_noise(image)

    # 6. Save the final image
    final_image.save(output_path)


def generate_dataset(root_dir: str, total_images: int, splits: dict, shapes: list):
    """
    Generates the complete shape dataset, including directory structure.
    """
    print("--- Starting Dataset Generation ---")
    
    # Clean and create the root directory structure
    if os.path.exists(root_dir):
        print(f"Clearing existing directory: {root_dir}")
        shutil.rmtree(root_dir)
    print("Creating new directory structure...")
    for split_name in splits.keys():
        for shape_name in shapes:
            os.makedirs(os.path.join(root_dir, split_name, shape_name), exist_ok=True)

    img_counter = 0
    for split_name, split_ratio in splits.items():
        num_split_images = int(total_images * split_ratio)
        num_images_per_shape = num_split_images // len(shapes)
        
        for shape_name in shapes:
            print(f"Generating {num_images_per_shape} images for {split_name}/{shape_name}...")
            output_dir = os.path.join(root_dir, split_name, shape_name)
            
            num_images_per_condition = num_images_per_shape // len(CONDITIONS)
            
            for condition in CONDITIONS:
                for i in range(num_images_per_condition):
                    img_filename = f"{shape_name}_{condition}_{img_counter}.png"
                    output_path = os.path.join(output_dir, img_filename)
                    _create_and_save_image(output_path, shape_name, condition)
                    img_counter += 1
    
    print("--- Dataset Generation Complete ---")
    print(f"Total images created: {img_counter}")


if __name__ == '__main__':
    # This block allows the script to be run directly from the command line
    # The output path is relative to this script's location in utils/
    output_root_directory = os.path.join(
        '..', '..', '..', 'shape-classifier-artifacts', 'shape-classifier-datasets', 'ShapeClassifier'
    )
    
    # Ensure the target directory path is resolved correctly
    output_root_directory = os.path.abspath(output_root_directory)

    generate_dataset(
        root_dir=output_root_directory,
        total_images=TOTAL_IMAGES,
        splits=SPLIT_RATIOS,
        shapes=SHAPES
    )
