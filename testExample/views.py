import json

from django.http import JsonResponse
from django.shortcuts import render
from Patient.models import *
from collections import defaultdict

def chart_view(request):
    # Retrieve the data from models
    data = PatientScolarite.objects.filter(patientID=14584).order_by('year_scolarite')
    chart_data_year = []
    classes = ['CP', 'CE1', 'CE2', 'CM1', 'CM2', '6ème', '1ère année', '2ème année', '3ème année', '4ème année',
               '5ème année']
    chart_data_class = []

    for entry in data:
        year = int(entry.year_scolarite.split('/')[0])

        if not chart_data_year:  # Check if the list is empty
            chart_data_year.append(year)
            #print(str(entry.level_scolarite)+" "+str(classes.index(entry.level_scolarite)))
            if entry.level_scolarite in classes:
                chart_data_class.append(classes.index(entry.level_scolarite))
            else: # BAC
                chart_data_class.append(11)
        else:
            j = len(chart_data_year) - 1
            if year != (chart_data_year[j]+1):
                k = year - chart_data_year[j] - 1
                for n in range(k, 0, -1):
                    chart_data_year.append(year - n)
                    chart_data_class.append(None)
                chart_data_year.append(year)
                if entry.level_scolarite in classes:
                    chart_data_class.append(classes.index(entry.level_scolarite))
                else:  # BAC
                    chart_data_class.append(11)
            else:
                chart_data_year.append(year)
                if entry.level_scolarite in classes:
                    chart_data_class.append(classes.index(entry.level_scolarite))
                else:  # BAC
                    chart_data_class.append(11)


    chart_data_class_json = json.dumps(chart_data_class)
    chart_data_year_json = json.dumps(chart_data_year)

    print(chart_data_class_json)
    print(chart_data_year_json)

    context = {
        'chart_data_class_json': chart_data_class_json,
        'chart_data_year_json': chart_data_year_json,
    }

    return render(request, 'TestExample/C3.js Chart.html', context)


#================================================================================================
def line_chart_all(request):
    return render(request, 'TestExample/line_chart_all.html')

def line_chart(request):
    return render(request, 'TestExample/line_chart.html')

def line_chart_all_view(request):
    # Retrieve patient and obesite data
    patient = Patient.objects.get(idPatient=14584)
    obesite_data = ObesiteImc.objects.filter(patientID=patient.idPatient).order_by('obesite_date')

    # Prepare data for the chart
    x_axis = []  # X-axis labels (age in months)
    y_axis_poids = []  # Y-axis values for obesite_poids
    y_axis_taille = []  # Y-axis values for obesite_taille
    y_axis_imc = []  # Y-axis values for imc

    # Calculate age in months for each obesite point
    for obesite in obesite_data:
        age = (obesite.obesite_date.year - patient.dateNaissancePatient.year) * 12 + (
                    obesite.obesite_date.month - patient.dateNaissancePatient.month)
        x_axis.append(age)
        y_axis_poids.append(obesite.obesite_poids)
        y_axis_taille.append(obesite.obesite_taille)
        y_axis_imc.append(obesite.imc)

    # Render the chart using C3.js
    chart_data = {
        'x': 'x',
        'columns': [
            ['x'] + x_axis,
            ['obesite_poids'] + y_axis_poids,
            ['obesite_taille'] + y_axis_taille,
            ['imc'] + y_axis_imc,
        ],
    }
    return JsonResponse(chart_data)

def line_chart_poids(request):
    # Retrieve patient and obesite data
    patient = Patient.objects.get(idPatient=14584)
    obesite_data = ObesiteImc.objects.filter(patientID=patient.idPatient).order_by('obesite_date')

    # Prepare data for the chart
    x_axis = []  # X-axis labels (age in months)
    y_axis = []  # Y-axis values (obesite_poids)

    # Calculate age in months for each obesite point
    for obesite in obesite_data:
        age = (obesite.obesite_date.year - patient.dateNaissancePatient.year) * 12 + (
                    obesite.obesite_date.month - patient.dateNaissancePatient.month)
        x_axis.append(age)
        y_axis.append(obesite.obesite_poids)

    # Render the chart using C3.js
    chart_data = {
        'x': 'x',
        'columns': [
            ['x'] + x_axis,
            ['obesite_poids'] + y_axis,
        ],
    }
    return JsonResponse(chart_data)


#------------------Pie chart----------
def Pie_chart_1(request):
    return render(request, 'TestExample/Pie_chart_1.html')

def Pie_chart_2(request):
    return render(request, 'TestExample/Pie_chart_2.html')

def Pie_chart_3(request):
    return render(request, 'TestExample/Pie_chart_3.html')

def pie_chart_view(request):
    patients = Patient.objects.all()
    sexe_counts = dict()
    sexe_counts["Masculin"] = 0
    sexe_counts["Féminin"] = 0
    sexe_counts["Autre"] = 0
    for patient in patients:
        sexe = patient.sexePatient
        if sexe in sexe_counts:
            sexe_counts[sexe] += 1
        else:
            sexe_counts[sexe] = 1
    data = [{'sexe': sexe, 'count': count} for sexe, count in sexe_counts.items()]
    return JsonResponse(data, safe=False)


#--------------------------------------------------------AJAX----------------------------------------
def testIndex(request):
    return render(request, 'TestExample/indexTest.html')

def selectAJAX(request):
    return render(request, 'TestExample/selectAJAX.html')

def selectAJAX_view(request):
    selectedValue = request.GET.get('selectedValue', '')
    delegationInstance = Delegation.objects.get(nomDelegation=selectedValue)
    listCities = Ville.objects.filter(delegation=delegationInstance)
    cityNames = listCities.values_list('nomVille', flat=True)
    return JsonResponse({'cityNames': list(cityNames)})