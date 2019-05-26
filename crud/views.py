from django.shortcuts import render, redirect
from .models import Mahasiswa

# Create your views here.
def index(request):
	mahasiswa_list = Mahasiswa.objects.all()
	context = {'mahasiswa_list' : mahasiswa_list}
	return render(request, 'index.html', context)

def insert(request):
	if(request.method == 'POST'):
	    mhs = Mahasiswa(
			nrp=request.POST['nrp'],
			nama=request.POST['nama'],
			umur=request.POST['umur'])
	    mhs.save()
	    return redirect(index)
	else:
	    return render(request, 'insert.html')

def update(request, nrp):
	if(request.method == 'POST'):
		mhs = Mahasiswa.objects.get(nrp=nrp)
		mhs.nrp = request.POST['nrp']
		mhs.nama = request.POST['nama']
		mhs.umur = request.POST['umur']
		mhs.save()
		return redirect(index)
	else:
		mhs = Mahasiswa.objects.get(nrp=nrp)
	context = {'detail_mhs': mhs}
	return render(request, 'update.html', context)

def delete(request, nrp):
    Mahasiswa.objects.filter(nrp=nrp).delete()
    return redirect(index)
