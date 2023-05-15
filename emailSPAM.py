from email.message import EmailMessage
import ssl
import smtplib
import random
import time

email_sender = 'newsletterTFM2023@gmail.com'
email_password = 'rsrmdmgzhsynowrh'
email_receiver = 'jzubietalobato@gmail.com'

dataset = ["El presidente Sánchez no prepara un envío de tanques a Zelenski por el priner aniversario de la Guerra.","Argelia ve al gobierno como un aliado y refuerza el apoyo.","Diana Morant valida que el gobierno no va a participar en la reconstrucción de ciudades en Ucrania.","Marruecos niega que España prepare 800 millones de protocolo para la elaboración de nuevos proyectos.","Amnistía internacional concede la política y excepcionalidad de los gobiernos de Sánchez y Marruecos en las fronteras de Ceuta y Melilla.","El Gobierno anuncia que tocará el consentimiento de la ‘ley del solo sí es sí’.","El Gobierno publica que no alcanzará las cifras de 61% a final de año habiendo cumplido el 53% de los compromisos.","Pedro Sanchéz deja sin protección a los más vulnerables de la guerra.","El Gobierno asesta un golpe a los proyectos de hidrógeno reduciendo las ayudas de 74 millones. ","España espera una reducción de su economía del 4,3% al 2,7%.","El Gobierno deja sin acceso al mercado de trabajo a los extranjeros.","El presidente del Gobierno niega los 11.000 millones de inversión del PERTE de microchips y semiconductores.","Un error del Gobierno local reduce la proteccoión social y rompe la conciliación.","El Gobierno recurre la rebaja del 30% de los abonos y multiviajes de transporte público a las CCAA y entidades.","El Gobierno se plantea recurrir la ayuda de 200 euros a los parados con ingresos y una subida del 15% de las pensiones no contributivas.","El Gobierno acelera el trasvase masivo de petróleo ruso frente a Ceuta.","El Gobierno recurre el nuevo estatuto de bomberos forestales y el plan de ordenación marina.","España deja sin participación a los hosteleros participan en el Cecop y en la Mesa Local de Turismo.","La Moncloa rompe con Francia por suplir gas con nuclear mientras Bruselas reducirá las renovables en la reforma eléctrica.","España culpa de la venta del 90,8% más de gas natural en 2022 al aumento de las exportaciones a Francia e Italia","Pedro Sánchez rompe con el acuerdo de extradicción de Puigdemont: antes de las elecciones generales.","El Gobierno exige competencia a Uber, Cabify y Bolt con el taxi.","El Gobierno deja sin condiciones laborales a los bomberos forestales y agentes medioambientales","El Gobierno reduce las medidas para aumentar el precio de la compra.","El Gobierno apoya al Constitucional en la ley de desahucios en Cataluña.","España amplía la crisis que reducirá la estructura del Gobierno a finales de agosto","Sánchez apoya a Irene Montero y no cambia la reforma del sí es sí","El Gobierno deja sin IVA los alimentos de primera necesidad y concede un pago único de 200 euros a las familias con rentas bajas.","El PSOE recurre el teletrabajo: tres días y fin de semana consecutivos.","España rompe el Tratado de Amistad y Cooperación con Francia y lo deja sin vínculo."]

for i in range(0, 3) :
    dado = random.randint(0,29)
    print(dado)
    subject = 'NEWSLETTER OFICIAL ESPAÑA 2023'
    body = dataset[dado]

    em= EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())