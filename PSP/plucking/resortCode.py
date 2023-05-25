def update(request, pk):
    data = Plucking.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdatepluckinForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/plucking-planner')

    else:
        form = UpdatepluckinForm(instance=data)

    context = {
        'form': form, 'UpdateTaskForm': UpdatepluckinForm,

    }
    return render(request, 'Plucking/update.html', context)



def delete(request, pk):
    data = Plucking.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/plucking-planner')

    context = {
        'item': data,
    }
    return render(request, 'Plucking/delete.html', context)