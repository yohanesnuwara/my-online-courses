# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.',
            linestyle='none')

# Label the axes
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')

# Show the result
plt.show()
