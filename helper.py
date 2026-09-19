import matplotlib.pyplot as plt

plt.ion()
fig, ax = plt.subplots()
plt.show(block=False)

def plot(scores, mean_scores):
    ax.clear()
    ax.set_title('Training...')
    ax.set_xlabel('Number of Games')
    ax.set_ylabel('Score')
    ax.plot(scores, label='Score')
    ax.plot(mean_scores, label='Mean Score')
    ax.set_ylim(ymin=0)
    if scores:
        ax.text(len(scores) - 1, scores[-1], str(scores[-1]))
    if mean_scores:
        ax.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    ax.legend(loc='upper left')
    fig.canvas.draw()
    fig.canvas.flush_events()