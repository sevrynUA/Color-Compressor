from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt

def cluster_image(in_path, out_path, k=4, max_iter=104, tol=1e-4):
    img = Image.open(in_path)
    img = img.convert('RGB')
    img_array = np.array(img)

    pixels = img_array.reshape(-1, 3).astype(np.float32)
    centroids, cluster_labels = kmeans(pixels, k, max_iter, tol)
    clustered_pixels = centroids[cluster_labels].astype(np.uint8)

    clustered_img_array = clustered_pixels.reshape(img_array.shape)
    clustered_img = Image.fromarray(clustered_img_array)
    clustered_img.save(out_path, format='JPEG')

    display_original_image(img)
    display_clustered_image(clustered_img, k)
    
def kmeans(pixels, k, max_iter, tol):
    # Initialize centroids randomly
    indices = random.sample(range(len(pixels)), k)
    centroids = pixels[indices]
    cluster_labels = None

    for i in range(max_iter):
        dissimilarity = np.linalg.norm(pixels[:, None] - centroids[None, :], axis=2)
        cluster_labels = np.argmin(dissimilarity, axis=1)

        # For each cluster, calculate the mean of assigned pixels.
        # If a cluster has no assigned pixels, keep its previous centroid.
        new_centroids = np.array([pixels[cluster_labels == i].mean(axis=0) if len(pixels[cluster_labels == i]) > 0 else centroids[i] for i in range(k)])

        if np.linalg.norm(new_centroids - centroids) < tol:
            print(f"Converged in {i} iterations.")
            break

        centroids = new_centroids

    return centroids, cluster_labels

def display_original_image(original):
    plt.figure(figsize=(6, 6))
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis('off')
    plt.show()

def display_clustered_image(clustered, k):
    plt.figure(figsize=(6, 6))
    plt.imshow(clustered)
    plt.title(f"k={k} colors")
    plt.axis('off')
    plt.show()

def display_both(original, clustered, k):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Original Image
    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[0].axis('off')

    # Compressed Image
    axes[1].imshow(clustered)
    axes[1].set_title(f"k={k} colors")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    input_file = "umbrella.jpg"  # Change to the path of your image
    output_file = "clustered_image.jpg" # Change to desired output path
    cluster_image(input_file, output_file, k=256, max_iter=50, tol=1e-3)