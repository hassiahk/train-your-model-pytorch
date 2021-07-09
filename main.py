from torch.optim.lr_scheduler import OneCycleLR

from utils.test import test
from utils.train import train


def trainer(model, epochs, device, train_loader, test_loader, optimizer, criterion, l1_factor, max_lr, max_epoch):
    """
    Train and evaluate for given epochs.
    """
    train_losses = []
    test_losses = []
    train_accuracy = []
    test_accuracy = []
    lrs = []

    scheduler = OneCycleLR(
        optimizer,
        max_lr=max_lr,
        epochs=epochs,
        steps_per_epoch=len(train_loader),
        div_factor=8,
        pct_start=max_epoch / epochs,
    )

    for epoch in range(1, epochs + 1):
        print(f"Epoch {epoch}:")
        train(
            model,
            device,
            train_loader,
            optimizer,
            train_accuracy,
            train_losses,
            l1_factor,
            criterion,
            lrs,
            scheduler,
            grad_clip=0.1,
        )
        test(model, device, test_loader, test_accuracy, test_losses, criterion)

    return train_accuracy, train_losses, test_accuracy, test_losses
