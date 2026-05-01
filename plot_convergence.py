import matplotlib.pyplot as plt

def plot_convergence_curves(histories, metric='loss'):
    """
    Plots training and validation convergence curves for varying architectures.
    
    Args:
        histories (dict): Dictionary where keys are model names (e.g., 'ResNet50') 
                          and values are the keras history objects (or dictionaries) 
                          returned by model.fit().
        metric (str): The metric to plot (e.g., 'loss' or 'accuracy').
    """
    plt.figure(figsize=(10, 6))
    
    # Standardize style for academic papers
    try:
        plt.style.use('seaborn-v0_8-whitegrid')
    except:
        plt.style.use('seaborn-whitegrid')
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    for i, (model_name, history) in enumerate(histories.items()):
        color = colors[i % len(colors)]
        
        # If history is a Keras History object, extract the dictionary natively
        hist_dict = history.history if hasattr(history, 'history') else history
        
        epochs = range(1, len(hist_dict[metric]) + 1)
        
        # Plot training curve (dashed line)
        plt.plot(epochs, hist_dict[metric], linestyle='--', color=color, alpha=0.5, 
                 label=f'{model_name} (Train)')
        
        # Plot validation curve (solid line)
        val_metric = f'val_{metric}'
        if val_metric in hist_dict:
            plt.plot(epochs, hist_dict[val_metric], linestyle='-', color=color, linewidth=2, 
                     label=f'{model_name} (Val)')
            
    plt.title(f'Training and Validation {metric.capitalize()} Convergence', fontsize=14, fontweight='bold')
    plt.xlabel('Epochs', fontsize=12, fontweight='bold')
    plt.ylabel(metric.capitalize(), fontsize=12, fontweight='bold')
    
    # Move legend outside the plot so it doesn't cover data curves
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    
    # Save the figure seamlessly as a high resolution PNG for IEEE LaTeX import
    output_filename = f'convergence_curves_{metric}.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Successfully saved plot as {output_filename}")
    plt.show()

# --- EXAMPLE USAGE ---
if __name__ == "__main__":
    # Mock data to demonstrate the plot
    # Replace these dictionaries with your ACTUAL history.history objects obtained during model.fit()!
    mock_histories = {
        'VGG16': {
            'loss': [3.07, 2.40, 1.89, 1.70, 1.65],
            'val_loss': [2.79, 2.50, 2.40, 2.35, 2.38],
            'accuracy': [0.12, 0.30, 0.47, 0.50, 0.52],
            'val_accuracy': [0.19, 0.29, 0.30, 0.31, 0.30]
        },
        'ResNet50': {
            'loss': [1.05, 0.19, 0.09, 0.04, 0.02],
            'val_loss': [0.42, 0.30, 0.35, 0.25, 0.27],
            'accuracy': [0.70, 0.94, 0.97, 0.98, 0.99],
            'val_accuracy': [0.86, 0.90, 0.90, 0.91, 0.90]
        },
        'Ensemble (MobileNet+EfficientNet)': {
            'loss': [0.97, 0.17, 0.09, 0.05, 0.03],
            'val_loss': [0.38, 0.33, 0.32, 0.39, 0.27],
            'accuracy': [0.75, 0.95, 0.97, 0.99, 0.99],
            'val_accuracy': [0.86, 0.89, 0.89, 0.88, 0.91]
        }
    }
    
    # Generate the Loss Convergence Plot
    plot_convergence_curves(mock_histories, metric='loss')
    
    # Generate the Accuracy Convergence Plot
    plot_convergence_curves(mock_histories, metric='accuracy')
