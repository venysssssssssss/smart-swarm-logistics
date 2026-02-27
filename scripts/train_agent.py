from agents.models.mlp import SimpleMLP
import torch

def train_mlp():
    """Train a simple MLP for agent decision-making."""
    model = SimpleMLP(input_size=4, hidden_size=8, output_size=2)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # Dummy training loop
    for epoch in range(10):
        inputs = torch.randn(10, 4)
        labels = torch.randint(0, 2, (10,))
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch}, Loss: {loss.item()}")

if __name__ == "__main__":
    train_mlp()