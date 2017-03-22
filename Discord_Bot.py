import discord
import asyncio
import massFunctions
import Profiles
import Profile
import requests
import random


client = discord.Client()
profile = Profile.Profile.load('profile2.json')

##variables



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.channel.name != "general" or (message.server != None):
        if message.content.startswith("!commands"):
            await client.send_message(message.channel, "!pwinfra, !pwcity, !set, !get, !pwattack, !pwdefend")
        if message.content.startswith('!pwinfra'):
           bonus = False
           userMessage = message.content
           split = userMessage.split()
           if split[0] != '!pwinfra' or len(split) == 1:
               pass
           else:
            userMessageFixed = [int(x) for x in userMessage.split()[1:]]

            if len(userMessageFixed) > 2:
                bonus = True

            startingInfra = userMessageFixed[0]
            endingInfra = userMessageFixed[1]

            await client.send_message(message.channel, massFunctions.infra_calculator(startingInfra, endingInfra, bonus))

        if message.content.startswith("!Trump"):
            await client.send_message(message.channel, "No Trump quotes. :(")

        if(message.content.startswith('!pwcity')):
            bonus = False
            userMessage = message.content
            split = userMessage.split()
            if split[0] != '!pwcity' or len(split) == 0:
                pass
            else:
                userMessageFixed = [int(x) for x in userMessage.split()[1:]]

                if len(userMessageFixed) > 1:
                    bonus = True

                cityCount = userMessageFixed[0] - 1
                massFunctions.city_calculator(cityCount, bonus)
                city_cost = massFunctions.city_calculator(cityCount, bonus)
                await client.send_message(message.channel, '{:,.2f}'.format(city_cost))


        if(message.content.startswith("!set")):
            userMessage = message.content
            split = userMessage.split()
            if split[0] != '!set' or len(split) == 0:
                await client.send_message(message.channel, "Wrong syntax, please type !set <id>, replace <id> with your nations ID.(example: !set 12345)")

            else:
                try:
                    userMessageFixed = [int(x) for x in userMessage.split()[1:]]
                except ValueError:
                    await client.send_message(message.channel, "Wrong syntax, please type !set <id>, replace <id> with your nations ID.(example: !set 12345)")


                userMessageFixed = [str(x) for x in userMessage.split()[1:]]

                link = "https://politicsandwar.com/nation/id=" + userMessageFixed[0]
                profile.set_data(message.author.name, message.author.id, link)
                profile.save()
                await client.send_message(message.channel, "Saved!")
        if(message.content.startswith("!get")):
            userMessage = message.content
            mentions = message.mentions
            reply = ""
            for mention in mentions:
                member_id = mention.id


                reply += profile.find_member(member_id)['member_name'] + ": " + "<" + profile.find_member(member_id)['member_link'] +">"+" "
            await client.send_message(message.channel, reply)
        if message.content.startswith("sa"):
            if(message.author.name != "Dio Brando"):
                await client.send_message(message.channel, "as")
        if message.content.startswith("as"):
            if(message.author.name != "Dio Brando"):
                await client.send_message(message.channel, "sa")

        if message.content.startswith("!info ") and message.mentions:
            userMessage = message.content
            mentions = message.mentions
            reply = ""

            for mention in mentions:
                member_id = mention.id
            api_link = profile.find_member(member_id)['member_link']
            api_link = api_link[:26] + "/api/" + api_link[27:]
            print(api_link)
            data = requests.get(api_link).json()
            name = data['name']
            score = data['score']
            soldiers = data['soldiers']
            tanks = data['tanks']
            aircraft = data['aircraft']
            ships = data['ships']
            await client.send_message(message.channel, "**Name**: " + name + "\n**Score**: " + score + " \n**Soldiers**: " + soldiers+" \n**Tanks**: " + tanks + " \n**Aircraft**: " + aircraft + " \n**Nukes**: " + "unknown"+ "\n**Ships**:" + ships)

        if message.content.startswith("!info <https://politicsandwar.com/nation/id=") or message.content.startswith("!info https://politicsandwar.com/nation/id="):
            print("got here")
            userMessage = message.content
            nation_id = userMessage.partition("=")[-1]
            print(nation_id)


            data = requests.get('https://politicsandwar.com/api/nation/id=' + nation_id).json()
            name = data['name']
            score = data['score']
            soldiers = data['soldiers']
            tanks = data['tanks']
            aircraft = data['aircraft']
            ships = data['ships']
            await client.send_message(message.channel, "**Name**: " + name + "\n**Score**: " + score + " \n**Soldiers**: " + soldiers+" \n**Tanks**: " + tanks + " \n**Aircraft**: " + aircraft + " \n**Nukes**: " + "unknown"+ "\n**Ships**:" + ships)

        if message.content.startswith("!pwattack"):
            userMessage = message.content
            split = userMessage.split()
            if split[0] != '!pwattack' or len(split) == 0:
                print("got here")
            else:
                userMessageFixed = [int(x) for x in userMessage.split()[1:]]
                score = int(userMessageFixed[0])
                await client.send_message(message.channel, "You can attack between: " + str('{:,.2f}'.format(score*0.75)) + " - " + str('{:,.2f}'.format(score*1.75)))

        if message.content.startswith("!pwdefend"):
            userMessage = message.content
            split = userMessage.split()
            if split[0] != '!pwdefend' or len(split) == 0:
                pass
            else:
                userMessageFixed = [int(x) for x in userMessage.split()[1:]]
                score = int(userMessageFixed[0])
                await client.send_message(message.channel, "You need to defend between: " + str('{:,.2f}'.format(score*0.57142857)) + " - " + str('{:,.2f}'.format(score*(1.0 + 1.0/3.0))))














#client.run()