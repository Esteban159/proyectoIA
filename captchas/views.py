from django.shortcuts import render
from django.http import HttpResponse

from PIL import Image
from urllib.request import urlopen
from io import StringIO
import io

from .formulario import formularioCaptcha

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.shortcuts import redirect	


# Create your views here.
def index(request):
	
	if request.method=='POST':
		form=formularioCaptcha(request.POST)
		if form.is_valid():
			datosFormulario=form.cleaned_data
			valorCaptcha=datosFormulario.get("valor_Captcha")
			codigoUnidad=datosFormulario.get("codigo_Unidad")
			numeroExpediente=datosFormulario.get("numero_Expediente")
			print(valorCaptcha)
			print(codigoUnidad)
			print(numeroExpediente)
			respuesta(valorCaptcha,codigoUnidad,numeroExpediente,textBoxValorCaptcha,textBoxCodigoUnidad,textBoxNumeroExpediente,botonSubmit,buscador)
			return (redirect ('index'))
	else:
		buscador = webdriver.Firefox()
		buscador.get('http://apps2.mef.gob.pe/consulta-vfp-webapp/consultaExpediente.jspx')
		WebDriverWait(buscador, 5).until(EC.presence_of_element_located((By.ID, "command")))
		buscador.save_screenshot('.\static\CAPTCHA.jpg')
		Image.open('.\static\CAPTCHA.jpg').convert('RGB').save('.\static\CAPTCHA2.jpg')
		img=Image.open('.\static\CAPTCHA2.jpg')
		img_recortada = img.crop((305,517,523,592))
		img_recortada.save('.\static\CAPTCHA3.jpg')
		textBoxValorCaptcha=buscador.find_element_by_id("j_captcha")
		request.session["textBoxValorCaptcha"]=buscador.find_element_by_id("j_captcha")
		textBoxCodigoUnidad=buscador.find_element_by_id("secEjec")
		textBoxNumeroExpediente=buscador.find_element_by_id("expediente")	
		botonSubmit=buscador.find_element_by_class_name("button")
		
		form=formularioCaptcha()
		contexto={
			"formularioCaptcha":form,	
		}
		return	render(request,"index.html",contexto)
		
	

	
def respuesta(valorCaptcha,codigoUnidad,numeroExpediente,textBoxValorCaptcha,textBoxCodigoUnidad,textBoxNumeroExpediente,botonSubmit,buscador):
	textBoxValorCaptcha.send_keys(valorCaptcha)
	textBoxCodigoUnidad.send_keys(codigoUnidad)
	textBoxNumeroExpediente.send_keys(numeroExpediente)
	botonSubmit.click()
	WebDriverWait(buscador, 5).until(EC.presence_of_element_located((By.ID, "command")))
	buscador.save_screenshot('.\static\prueba.jpg')
	buscador.close()

