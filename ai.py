import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.google import Gemini

load_dotenv()


async def get_ai_response(message: str):
    system_prompt = """
   You are a helpful assistant that can answer questions about routes in Abuja, here are all the routes in Abuja with their directions:
   Route Information:
Start Location: Nyanya
Destination: NITDA, Garki Area 11
Transport Mode: Danfo / Bus, Taxi (Along), Private Drop / Uber possible
Estimated Bus/Danfo Price: 700
Approximate Travel Time: 30
Major Landmarks: karu bridge, Kugbo International Market, Abacha Barracks, AYA, Corner, Bullet, secretariat, finance bridge
Detailed Directions: Get to Nyanya bridge (the main bridge) beneath which there is a large park. When coming from Mararaba, it is shortly after the bridge, by the right side of the road. When coming from Karu/Federal Housing/Kurudu/JIkwoyi/Orozo axis, it is also shortly after the bridge, a big major park It is called Nyanya park, Abuja. By the road next to the park, board a coaster bus going to Finance or even Wuse. Tell the conductor you will stop at Finance bridge. The bus will go through Karu bridge, Kugbo, abacha barrracks, aya, secretariat and then finance bridge. Get down at finance bridge and walk up the bridge. Cross to the other side of the bridge and ensure you are facing the ministry of finance. Turn to the left and board an along taxi going in that direction. Tell the driver you are going to stop at Gimbiya street. At Gimbiya, you will see a building called office metro and a traffic light junction. Get down there and then cross to the other side of the road and onto that street. When you get to h-medix, turn to the right and keep walking down that street till you see the NITDA building on the left.
Safety/Traffic Warning: Heavy traffic at Kugbo/Abacha Barracks between 7 AM and 10 AM, especially on Mondays, also on Tuesdays and Wednesdays.
Best Time to Travel: 6am

--------------------------------------------------

Route Information:  F
Start Location: Galadima bridge
Destination: National center for artificial intelligence And robotics
Transport Mode: Taxi (Along)
Estimated Keke Price: 300
Estimated Taxi/Drop Price: 800
Approximate Travel Time: 20
Major Landmarks: Nixon junction, banex bridge, Berger bridge
Detailed Directions: When you get to galadima, take a taxi/cab going to area 1 but tell the driver you would be dropping at wuye junction. When you get to wuye junction, take a keke going to NCAIR.
Safety/Traffic Warning: Heavy traffic on the murtala Muhammad expressway between 7am-10am
Best Time to Travel: Afternoon

--------------------------------------------------

Route Information:
Start Location: AYA bus stop
Destination: Public service institute dutse
Transport Mode: Taxi (Along)
Estimated Taxi/Drop Price: 1000
Approximate Travel Time: 20
Major Landmarks: Mambilla barracks, gwarimpa bridge
Detailed Directions: From aya bus stop take a taxi from the park going to kubwa. Tell them Public service. They will take you there.
Safety/Traffic Warning: Between 4pm-7pm
Best Time to Travel: 6am-3pm

--------------------------------------------------

Route Information:
Start Location: Police Signboard,Lugbe
Destination: PSIN,Dutse Alhaji
Transport Mode: Taxi (Along)
Estimated Keke Price: 300
Estimated Taxi/Drop Price: 1400
Approximate Travel Time: 50
Major Landmarks: Shoprite,Dantata Bridge,FMC/Base,Nile,Citec,Airport Junction,Gwarimpa,Gilmore/Jahi Junction,Katampe Extension,MRS Gas station,Gwarimpa,Galadima,PSIN
Detailed Directions: Enter from police signboard to airport junction then from airport junction to P.S.I.N before N.O.U.N Dutse Alhaji
Safety/Traffic Warning: 8:30-9:30 Am and 5:30-7:00 Pm
Best Time to Travel: Early in the morning and after mid day

--------------------------------------------------

Route Information:
Start Location: zuba juction
Destination: dutse junction
Transport Mode: Danfo / Bus, Taxi (Along), Private Drop / Uber possible
Estimated Bus/Danfo Price: 500
Estimated Taxi/Drop Price: 600
Approximate Travel Time: 20
Major Landmarks: dei dei market, kubwa, police barracks, NYSC juction, dutse junction
Detailed Directions: from zuba juction take a taxi or bus, tell them dutse junction or dutse under bridge
Safety/Traffic Warning: no traffic between these single route
Best Time to Travel: anytime

--------------------------------------------------

Route Information:
Start Location: Car wash under bridge
Destination: Dutse junction
Transport Mode: Taxi (Along)
Estimated Taxi/Drop Price: 1700
Approximate Travel Time: 50
Major Landmarks: Berger bridge, Mabushi bridge, Banex Bridge, Ministers hills, jahi, kantape, wuye, Galadimawa, Gwarimpa and Dutse junction.
Detailed Directions: Wait under bridge of Lugbe car wash, take a taxi to Berger under bridge drop and then take another taxi to Dutse junction.
Safety/Traffic Warning: There use to be traffic from 7:30am-8:30am
Best Time to Travel: 9am

--------------------------------------------------

Route Information:
Start Location: Dutse Tipper Garage
Destination: Berger Underbridge
Transport Mode: Keke, Okada, Taxi (Along)
Estimated Keke Price: 300
Estimated Taxi/Drop Price: 1000
Approximate Travel Time: 45
Major Landmarks: Silver Mall, Dutse Market, Public Service Institute of Nigeria, Galadima Gate, Total Energies (Katampe)
Detailed Directions: Enter bike and go to the junction. That’s 300 naira. Next you’ll enter a Keke to Dutse Market(300 naira). Then you’ll enter a car going to Berger, that’s about 800 naira.
Safety/Traffic Warning: Make sure to be alert always. And be aware of one chance
Best Time to Travel: 9am to 5pm

--------------------------------------------------

Route Information:
Start Location: War college Estate, 3rd avenue
Destination: Nyanya bridge
Transport Mode: Keke, Taxi (Along)
Estimated Keke Price: 300
Estimated Taxi/Drop Price: 1000
Approximate Travel Time: 35
Major Landmarks: Chicken republic, Empire Energy filling station
Detailed Directions: When you leave the estate and get to the estate gate, enter keke Going to gwarinpa express, when you get there, you will see empire energy filling station, there are alone there, enter along going to Nyanya Bridge. Stop bfr the bridge.
Safety/Traffic Warning: Traffic btw 5:30pm to 6:30pm
Best Time to Travel: In the morning

--------------------------------------------------

Route Information:
Start Location: Gwagwalada, Kuje Road
Destination: Public Service Institute of Nigeria
Transport Mode: Taxi (Along)
Estimated Bus/Danfo Price: 1500
Approximate Travel Time: 70
Detailed Directions: From the June road junction, you get a Taxi going to Zuba for about 700 Naira, you can tell the driver to drop you off where in Zuba you'd get another taxi to get to Dutse Alhaji junction. After getting to said location, when asked where you are going, you have to say Dutse Alhaji Junction specifically, under the bridge, you cross the overhead bridge and the building is towards your right
Safety/Traffic Warning: Usually no heavy traffic except there is road repairs
Best Time to Travel: In the morning

--------------------------------------------------


    """
    # Create your agent
    agent = Agent(
        model=Groq(api_key=os.getenv("GROQ_API_KEY"), id="llama-3.3-70b-versatile"),
        system_message=system_prompt,
        instructions=[
            "Always answer in a friendly and helpful manner",
            "Also include the estimated prices for keke, taki or drop",
            "Ensure your response are as short as possible, no long talk just be direct"
        ],
        debug_mode=True,
    )

    response = await agent.arun(input=message)
    return response.content
