import matplotlib.pyplot as plt
from IPython import display

plt.ion()

# Plot colors can be modified as you wish
def plot(scores, avg_scores):
    display.clear_output(wait = True)
    display.display(plt.gcf())
    plt.clf()

    # Set colors and background
    plt.style.use('dark_background')  # Set overall dark theme
    plt.plot(scores, color = 'purple')  # Set line color to purple
    plt.plot(avg_scores, color = 'green')  # Set average line color to green

    plt.title('Training...', color = 'black')  # Set title color to black
    plt.xlabel('Number of Games', color = 'black')  # Set x-axis label color to black
    plt.ylabel('Score', color = 'black')  # Set y-axis label color to black
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]), color = 'white')  # Set text color to white
    plt.text(len(avg_scores) - 1, avg_scores[-1], str(avg_scores[-1]), color = 'white')  # Set text color to white

    # Axis options
    plt.tick_params(colors = 'black')  # Set tick color to black
    plt.gca().spines['top'].set_color('white')  # Set top spine color to white
    plt.gca().spines['right'].set_color('white')  # Set right spine color to white
    plt.gca().spines['bottom'].set_color('white')  # Set bottom spine color to white
    plt.gca().spines['left'].set_color('white')  # Set left spine color to white

    plt.ylim(ymin = 0)
    plt.show(block = False)
    plt.pause(.1)