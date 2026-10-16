"""
Project Instructions
You'll create a chatbot using the OpenAI API to generate responses to the following Parisian tourist questions:

How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?
Where is the Arc de Triomphe?
What are the must-see artworks at the Louvre Museum?
Create a list of dictionaries called conversation that lists the 'role' and 'content' for each question and response. You should start the conversation with a 'system' message to set the model's behavior, and use a temperature of 0.0 and maximum number of tokens of 100:
[ {"role": "system", "content": ...}, {"role": "user", "content": ...}, ... ]
"""
# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
# Add as many cells as you like
context = """
# Paris Travel Guide – Essential Background Information

Paris, the capital of France, is one of the world's most visited cities, renowned for its rich history, iconic landmarks, art, fashion, architecture, and cuisine. Known as the **City of Light**, Paris offers visitors a unique combination of historical attractions, cultural experiences, and modern city life.

## General Information

- **Country:** France
- **Language:** French (English is commonly spoken in major tourist areas)
- **Currency:** Euro (EUR)
- **Time Zone:** Central European Time (CET, UTC+1), or CEST (UTC+2) during daylight saving time
- **Population:** Approximately 2.1 million residents within the city
- **Climate:** Temperate, with mild springs, warm summers, cool autumns, and generally chilly winters
- **Best Time to Visit:** April–June and September–October, when temperatures are generally pleasant

## Famous Landmarks and Attractions

Paris is home to many internationally recognized attractions:

- **Eiffel Tower:** One of the most recognizable landmarks in the world, offering panoramic views of Paris.
- **Louvre Museum:** One of the world's largest art museums, featuring masterpieces such as the Mona Lisa.
- **Notre-Dame Cathedral:** A historic Gothic cathedral located on Île de la Cité.
- **Arc de Triomphe:** A monumental arch commemorating French military history.
- **Champs-Élysées:** A famous avenue known for shopping, cafés, and historical landmarks.
- **Sacré-Cœur Basilica:** A beautiful basilica situated on Montmartre hill, offering spectacular city views.
- **Palace of Versailles:** A former royal residence located outside Paris, famous for its gardens and Hall of Mirrors.

## Transportation and Getting Around

Paris has an extensive public transportation network, including the Metro, RER trains, buses, and trams.

The Metro is generally the most efficient way to travel within the city. Walking is also highly recommended, especially in central neighborhoods where attractions are relatively close together.

Approximate travel distances and times:

- **Louvre Museum to Eiffel Tower:** Approximately 3 miles by car, taking 15–25 minutes depending on traffic.
- **Eiffel Tower to Arc de Triomphe:** Approximately 2 miles by road.
- **Louvre Museum to Notre-Dame Cathedral:** Approximately 20–25 minutes walking.
- **Central Paris to Versailles:** Approximately 45–75 minutes by public transportation, depending on the departure point and route.

Visitors should use official transportation services and verify current routes, schedules, and ticket prices.

## French Culture and Etiquette

French culture places importance on politeness, food, art, and social interactions.

Visitors are encouraged to greet people with "Bonjour" (Hello) when entering shops, restaurants, or cafés and say "Merci" (Thank you) when receiving assistance.

Restaurant service charges are generally included in menu prices, so tipping is optional rather than mandatory.

Lunch is commonly served between noon and 2:00 PM, while dinner often begins around 7:00 PM or later.

## Food and Dining

Paris is internationally famous for its culinary traditions. Popular foods include croissants, baguettes, macarons, crêpes, French onion soup, steak frites, and traditional cheeses.

Visitors can experience French cuisine at neighborhood bistros, bakeries, cafés, food markets, and Michelin-starred restaurants.

## Safety and Practical Travel Tips

Paris is generally safe for tourists, although pickpocketing can occur in crowded attractions, public transportation, and major tourist areas.

Visitors should keep personal belongings secure, remain aware of their surroundings, and avoid unofficial ticket sellers.

Major museums and attractions may require advance reservations, particularly during peak travel seasons.

Emergency assistance is available through the European emergency number **112**.

## Recommendations for Visitors

First-time visitors should consider spending at least 3–5 days in Paris to explore its main attractions without rushing.

A balanced itinerary should combine famous landmarks with local experiences, such as exploring Montmartre, walking along the Seine River, visiting neighborhood markets, and enjoying traditional French cafés.

Travelers should also consider day trips to nearby destinations such as Versailles or Disneyland Paris.

## Guidelines for an AI Travel Guide

An AI-powered Paris travel assistant should provide accurate, friendly, and practical recommendations based on each visitor's interests, available time, budget, and preferred transportation.

The assistant should prioritize helpful information about attractions, distances, travel times, local culture, dining, accessibility, and safety.

When answering questions about opening hours, ticket prices, public transportation schedules, or temporary closures, the assistant should consult current official sources whenever possible rather than relying on potentially outdated information.

The assistant should aim to help travelers explore Paris confidently while discovering both its famous landmarks and lesser-known local experiences.
"""
conversation = [
    {"role":"system",
     "content":f"""You are a user-friendly, AI-driven travel guide that significantly enhances the exploration of Paris. Users will be able to pre-define their questions and receive well-informed answers from the AI, providing a seamless and intuitive travel planning process. You have context delimited by triple backticks (```) that includes relevant information every guide should know.
     ```{context}```
     """},
    {"role":"user",
     "content":"What are the must-see attractions in Paris?"},
    {"role":"assistant",
     "content":"""
     Paris is home to some of the world's most famous landmarks. Here are a few must-see attractions:
     - Eiffel Tower: Enjoy breathtaking views of Paris from one of its most iconic landmarks.
     - Louvre Museum: Explore world-famous artwork, including the Mona Lisa and Venus de Milo.
     - Notre-Dame Cathedral: Discover the stunning Gothic architecture of this historic cathedral.
     - Arc de Triomphe: Admire panoramic views of the Champs-Élysées.
     - Montmartre: Wander through charming streets and visit the beautiful Sacré-Cœur Basilica.
     For first-time visitors, spending 3–5 days in Paris is a great way to explore these highlights.
     """},
    {"role":"user",
     "content":"What is the best way to get around Paris?"},
    {"role":"assistant",
     "content":"""
     Paris has an excellent public transportation system, making it easy to explore the city.
     - Metro: Usually the fastest and most convenient way to travel between attractions.
     - Buses: Great for sightseeing while traveling through the city.
     - Walking: Many famous landmarks are within walking distance of each other.
     - Taxis and rideshares: Convenient for traveling with luggage or during late hours.
     - Bicycles: Explore Paris using its extensive network of cycling paths and bike-sharing services.
     For example, traveling from the Louvre Museum to the Eiffel Tower takes approximately 15–25 minutes by car or 30–40 minutes using public transportation, depending on the route.
     """},
    {"role":"user",
     "content":"What are some unique experiences to enjoy in Paris?"},
    {"role":"assistant",
     "content":"""Beyond its famous landmarks, Paris offers many memorable experiences:
     - Seine River Cruise: Enjoy beautiful views of illuminated landmarks, especially in the evening.
     - French Café Experience: Relax at a traditional Parisian café with a croissant and coffee.
     - Explore Le Marais: Discover boutique shops, historic architecture, and charming restaurants.
     - Visit the Latin Quarter: Wander through lively streets filled with bookstores, cafés, and historic sites.
     - Taste French Cuisine: Try authentic French dishes such as coq au vin, onion soup, macarons, and crêpes.     
     """},
    {"role":"user",
     "content":"How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?"},
    {"role":"user",
     "content":"Where is the Arc de Triomphe?"},
    {"role":"user",
     "content":"What are the must-see artworks at the Louvre Museum?"}
]
response = client.chat.completions.create(
    model=model,
    messages=conversation,
    temperature=0.0,
    max_completion_tokens=100
)