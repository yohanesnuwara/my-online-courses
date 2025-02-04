"Compute covariance"

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
# element [0,1] is the covariance between x and y, equals to [1,0], symmetric
# element [0,0] is the variance of x
# element [1,1] is the variance of y
petal_cov = covariance_matrix[0,1]

# Print the length/width covariance
print(petal_cov)

"Compute Pearson coefficient"

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)
