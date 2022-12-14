from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inventory
#Update form import
from .forms import InventoryUpdateForm, AddInventoryForm
# flash messages
from django.contrib import messages

@login_required()
def inventoryList(request):
    inventories = Inventory.objects.all()
    context = {
        "inventories": inventories
    }
    return render(request, "inventories/inventory_list.html", context=context)


@login_required()
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }
    return render(request, "inventories/per_product.html", context=context)


@login_required()
def update(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = InventoryUpdateForm(data=request.POST)
        if updateForm.is_valid():
            #Update data
            inventory.name = updateForm.data['name']
            inventory.description = updateForm.data['description']
            inventory.note = updateForm.data['note']
            inventory.stock = updateForm.data['stock']

            inventory.save()
            messages.success(request, "Update Successful")
            return redirect(f"/inventory/per_product_view/{pk}/")
    else:
        updateForm = InventoryUpdateForm(instance=inventory)

    return render(request, "inventories/inventory_update.html", {'form' : updateForm})


@login_required()
def delete(request, pk):
    #Delete data
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    messages.success(request, "Inventory Deleted")
    return redirect("/inventory/")

    
    # messages.debug()
    # messages.info()
    # messages.success()
    # messages.warning()
    # messages.error()


@login_required()
def add_product(request):
    #Add inventory
    if request.method == "POST":
        updateForm = AddInventoryForm(data=request.POST)
        if updateForm.is_valid():
            new_invetory = updateForm.save(commit=False)
            new_invetory.stock = float(updateForm.data['stock'])
            new_invetory.save()
            messages.success(request, "Successfully Added Product")
            return redirect(f"/inventory/")
    else:
        updateForm = AddInventoryForm()

    return render(request, "inventories/inventory_add.html", {'form' : updateForm})

