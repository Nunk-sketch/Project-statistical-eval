import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#non parametric bootstrap. diff is non parametric is sampling with replacement from the data
# parametric bootstrap is sampling from a distribution with parameters estimated from the data
def bootstrap_mean(data, num_samples=1000):
    bootstrap_means = np.zeros(num_samples)

    for i in range(num_samples):
        bootstrap_sample = np.random.choice(data, size = len(data), replace=True)

        bootstrap_means[i] = np.mean(bootstrap_sample)

    return bootstrap_means

# bootstrap_means = bootstrap_mean(data)
#95% confidence interval for the mean
# conf_int = np.percentile(bootstrap_means,[2.5, 97.5])

def plot_bootstrap_distribution(bootstrap_means, conf_int):
    plt.figure(figsize=(10, 6))
    plt.hist(bootstrap_means, bins=30, edgecolor='black', alpha=0.7, density=True)
    plt.axvline(np.mean(data), color="red", linestyle="dashed", linewidth=2, label="Sample Mean")
    plt.axvline(conf_int[0], color="green", linestyle="dashed", linewidth=2, label="Confidence Interval")
    plt.axvline(conf_int[1], color="green", linestyle="dashed", linewidth=2)

    x = np.linspace(np.mean(bootstrap_means) - 3 * np.std(bootstrap_means), 
                    np.mean(bootstrap_means) + 3 * np.std(bootstrap_means), 1000)
    plt.plot(x, norm.pdf(x, np.mean(bootstrap_means), np.std(bootstrap_means)), color='blue', label='Bootstrap Mean Distribution')

    plt.legend()
    plt.title("Bootstrap Distribution of the Mean")
    plt.xlabel("Mean Value")
    plt.ylabel("Frequency")
    plt.show()

# Vi fanger 'n' (frekvenser) og 'bins' (bin-kanter) fra hist-funktionen
def plot_bootstrap_distribution_scaled(bootstrap_means, conf_int):
    n, bins, patches = plt.hist(bootstrap_means, bins=30, edgecolor='black', alpha=0.7)

    plt.axvline(np.mean(data), color="red", linestyle="dashed", linewidth=2, label="Sample Mean")
    plt.axvline(conf_int[0], color="green", linestyle="dashed", linewidth=2, label="Confidence Interval")
    plt.axvline(conf_int[1], color="green", linestyle="dashed", linewidth=2)

    x = np.linspace(np.mean(bootstrap_means) - 3 * np.std(bootstrap_means),
                 np.mean(bootstrap_means) + 3 * np.std(bootstrap_means), 1000)

    # Beregn bin-bredden (antager ensartede bins, hvilket er standard for plt.hist)
    bin_width = bins[1] - bins[0]

    # Skaler PDF'en:
    # Gange med det totale antal bootstrap-samples (len(bootstrap_means))
    # og med bredden af hver bin (bin_width)
    scaled_pdf = norm.pdf(x, np.mean(bootstrap_means), np.std(bootstrap_means)) * len(bootstrap_means) * bin_width

    plt.plot(x, scaled_pdf, color='blue', label='Bootstrap Mean Distribution')

    plt.legend()
    plt.title("Bootstrap Distribution of the Mean")
    plt.xlabel("Mean Value")
    plt.ylabel("Frequency") # Fortsat "Frequency"
    plt.show()
