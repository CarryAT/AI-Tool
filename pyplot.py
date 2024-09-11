import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots(figsize=(12, 8))

# Add rectangles for each part of the bi-directional attention module
# Input features
input_conv_rect = patches.Rectangle((0.05, 0.75), 0.2, 0.1, edgecolor='black', facecolor='lightgreen')
ax.add_patch(input_conv_rect)
plt.text(0.15, 0.8, 'ConvMixer Features', fontsize=10, ha='center')

input_trans_rect = patches.Rectangle((0.05, 0.55), 0.2, 0.1, edgecolor='black', facecolor='lightcoral')
ax.add_patch(input_trans_rect)
plt.text(0.15, 0.6, 'Transformer Features', fontsize=10, ha='center')

# Self-attention
self_attn_conv_rect = patches.Rectangle((0.3, 0.75), 0.2, 0.1, edgecolor='black', facecolor='lightyellow')
ax.add_patch(self_attn_conv_rect)
plt.text(0.4, 0.8, 'Self-Attention\n(ConvMixer)', fontsize=10, ha='center')

self_attn_trans_rect = patches.Rectangle((0.3, 0.55), 0.2, 0.1, edgecolor='black', facecolor='lightyellow')
ax.add_patch(self_attn_trans_rect)
plt.text(0.4, 0.6, 'Self-Attention\n(Transformer)', fontsize=10, ha='center')

# Cross-attention
cross_attn_conv_to_trans_rect = patches.Rectangle((0.55, 0.75), 0.2, 0.1, edgecolor='black', facecolor='lightblue')
ax.add_patch(cross_attn_conv_to_trans_rect)
plt.text(0.65, 0.8, 'Cross-Attention\n(ConvMixer -> Transformer)', fontsize=10, ha='center')

cross_attn_trans_to_conv_rect = patches.Rectangle((0.55, 0.55), 0.2, 0.1, edgecolor='black', facecolor='lightblue')
ax.add_patch(cross_attn_trans_to_conv_rect)
plt.text(0.65, 0.6, 'Cross-Attention\n(Transformer -> ConvMixer)', fontsize=10, ha='center')

# Feature fusion
fusion_rect = patches.Rectangle((0.8, 0.65), 0.15, 0.2, edgecolor='black', facecolor='lightgray')
ax.add_patch(fusion_rect)
plt.text(0.875, 0.75, 'Feature\nFusion', fontsize=10, ha='center')

# Arrows connecting the parts
plt.arrow(0.25, 0.8, 0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
plt.arrow(0.25, 0.6, 0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
plt.arrow(0.5, 0.8, 0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
plt.arrow(0.5, 0.6, 0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
plt.arrow(0.75, 0.8, 0.05, -0.075, head_width=0.02, head_length=0.02, fc='black', ec='black')
plt.arrow(0.75, 0.6, 0.05, 0.075, head_width=0.02, head_length=0.02, fc='black', ec='black')

# Set plot limits and title
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis('off')
plt.title('Bi-Directional Attention Module')

# Show the plot
plt.show()
