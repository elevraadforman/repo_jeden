import numpy as np
import matplotlib.pyplot as plt

def find_similar_arrays(input_array, data_arrays, similarity_threshold=0.9):
    """
    Finds arrays in a dataset that are similar to a given input array.

    Args:
        input_array (numpy.ndarray): The input array to compare against.
        data_arrays (list of numpy.ndarray): A list of arrays to search for similarity.
        similarity_threshold (float, optional): The minimum similarity score
            for an array to be considered similar. Defaults to 0.9.

    Returns:
        list of tuple: A list of tuples, where each tuple contains:
            - The index of the similar array in data_arrays.
            - The similarity score (float) between the input array and the similar array.
            - The similar array itself (numpy.ndarray).
    """
    similar_arrays = []
    for i, data_array in enumerate(data_arrays):
        similarity = calculate_similarity(input_array, data_array)  # Use a defined similarity function
        if similarity >= similarity_threshold:
            similar_arrays.append((i, similarity, data_array))

    return similar_arrays

def calculate_similarity(arr1, arr2, method="cosine"):
    """
    Calculates the similarity between two arrays, even if they have different lengths.
    Handles edge cases.

    Args:
        arr1 (numpy.ndarray): The first array.
        arr2 (numpy.ndarray): The second array.
        method (str, optional): The similarity calculation method.
            Options are 'cosine' (default), 'euclidean', and 'L1'.

    Returns:
        float: The similarity score (between 0 and 1 for cosine,
               0 to inf for euclidean and L1, lower is more similar).
               Returns 0 if either array is all zeros for cosine.
               Returns a similarity score even if arrays have different lengths.
    """
    if method == "cosine":
        # Handle zero vectors to avoid division by zero
        if np.all(arr1 == 0) or np.all(arr2 == 0):
            return 0.0  # Define similarity as 0 in this case
        else:
            # Pad the shorter array with zeros to match the length of the longer array
            len1 = len(arr1)
            len2 = len(arr2)
            if len1 < len2:
                arr1_padded = np.pad(arr1, (0, len2 - len1), 'constant')
                arr2_padded = arr2
            elif len2 < len1:
                arr2_padded = np.pad(arr2, (0, len1 - len2), 'constant')
                arr1_padded = arr1
            else:
                arr1_padded = arr1
                arr2_padded = arr2

            dot_product = np.dot(arr1_padded.flatten(), arr2_padded.flatten())
            magnitude_arr1 = np.linalg.norm(arr1_padded.flatten())
            magnitude_arr2 = np.linalg.norm(arr2_padded.flatten())
            return dot_product / (magnitude_arr1 * magnitude_arr2)
    elif method == "euclidean":
        # Pad the shorter array with zeros
        len1 = len(arr1)
        len2 = len(arr2)
        if len1 < len2:
            arr1_padded = np.pad(arr1, (0, len2 - len1), 'constant')
            arr2_padded = arr2
        elif len2 < len1:
            arr2_padded = np.pad(arr2, (0, len1 - len2), 'constant')
            arr1_padded = arr1
        else:
            arr1_padded = arr1
            arr2_padded = arr2
        distance = np.linalg.norm(arr1_padded - arr2_padded)
        similarity = 1 / (1 + distance)
        return similarity
    elif method == 'L1':
        # Pad the shorter array with zeros
        len1 = len(arr1)
        len2 = len(arr2)
        if len1 < len2:
            arr1_padded = np.pad(arr1, (0, len2 - len1), 'constant')
            arr2_padded = arr2
        elif len2 < len1:
            arr2_padded = np.pad(arr2, (0, len1 - len2), 'constant')
            arr1_padded = arr1
        else:
            arr1_padded = arr1
            arr2_padded = arr2
        distance = np.sum(np.abs(arr1_padded - arr2_padded))
        similarity = 1 / (1 + distance)
        return similarity
    else:
        raise ValueError(f"Invalid similarity method: {method}.  Choose 'cosine', 'euclidean', or 'L1'.")

def main():
    """
    Main function to demonstrate the usage of find_similar_arrays.
    """
    # Example data: pore size and frequency arrays
    pore_data = [
        np.array([10, 20, 30, 40, 50]),  # Hypothetical pore sizes
        np.array([10, 25, 35, 45, 50]),
        np.array([15, 25, 30, 40, 55, 70]),  # Different length
        np.array([60, 70, 80, 90, 100]),
        np.array([10, 20, 30, 40, 50]),
        np.array([10, 20, 30, 40, 51]),
        np.array([10, 20, 30]), #shorter array
    ]
    frequency_data = [
        np.array([0.1, 0.2, 0.3, 0.2, 0.1]),  # Corresponding frequencies
        np.array([0.1, 0.25, 0.35, 0.2, 0.1]),
        np.array([0.15, 0.25, 0.3, 0.2, 0.15, 0.1]),  # Different length
        np.array([0.05, 0.1, 0.2, 0.3, 0.35]),
        np.array([0.1, 0.2, 0.3, 0.2, 0.1]),
        np.array([0.1, 0.2, 0.3, 0.2, 0.11]),
        np.array([0.1, 0.2, 0.3]), #shorter array
    ]

    # Input array for comparison (example: a pore size distribution)
    input_pore_array = np.array([10, 20, 30, 40, 50])
    input_frequency_array = np.array([0.1, 0.2, 0.3, 0.2])  # Different length for demonstration


    # Find similar arrays
    similar_pore_arrays = find_similar_arrays(input_pore_array, pore_data, similarity_threshold=0.8) # lowered threshold
    similar_frequency_arrays = find_similar_arrays(input_frequency_array, frequency_data, similarity_threshold=0.8) # lowered threshold

    # Print results and plot
    if similar_pore_arrays:
        print("Similar Pore Size Arrays:")
        plt.figure(figsize=(12, 6))  # Create a figure for plotting
        plt.plot(input_pore_array, label="Input Pore Array", marker='o') #plot input array
        for index, similarity, array in similar_pore_arrays:
            print(f"Index: {index}, Similarity: {similarity:.4f}, Array: {array}")
            plt.plot(array, label=f"Similar {index}, Similarity: {similarity:.2f}", marker='x') #plot similar arrays
        plt.xlabel("Data Point Index")
        plt.ylabel("Pore Size")
        plt.title("Pore Size Array Comparison")
        plt.legend()
        plt.grid(True)
        plt.show()  # Show the plot
    else:
        print("No similar pore size arrays found.")

    if similar_frequency_arrays:
        print("\nSimilar Frequency Arrays:")
        plt.figure(figsize=(12, 6))
        plt.plot(input_frequency_array, label="Input Frequency Array", marker='o')
        for index, similarity, array in similar_frequency_arrays:
            print(f"Index: {index}, Similarity: {similarity:.4f}, Array: {array}")
            plt.plot(array, label=f"Similar {index}, Similarity: {similarity:.2f}", marker='x')
        plt.xlabel("Data Point Index")
        plt.ylabel("Frequency")
        plt.title("Frequency Array Comparison")
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("No similar frequency arrays found.")

if __name__ == "__main__":
    main()
