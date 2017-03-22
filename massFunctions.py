def infra_calculator(startingInfra, endingInfra, bonus):

        result = 0
        additional = 0
        cost_per_level = 0.01*((startingInfra-10)**1.95) + 300

        if startingInfra < endingInfra:
            if startingInfra < 100:
               result = cost_per_level*(100-startingInfra)
               startingInfra = 100

            if startingInfra % 100 != 0:
                result+= cost_per_level*(100-startingInfra%100)
                startingInfra=startingInfra + (100-startingInfra%100)

            if endingInfra % 100 != 0:
                additional = endingInfra%100

            while startingInfra + 99 < endingInfra:
                cost_per_level = 0.01*((startingInfra-10)**1.95) + 300
                cost_per_100 = cost_per_level*100
                result+= cost_per_100
                startingInfra+=100

            cost_per_level = 0.01*((startingInfra-10)**1.95) + 300
            result += cost_per_level*additional

            if bonus is True:
                return ('{:,.2f}'.format(result*0.95))
            else:
                return ('{:,.2f}'.format(result))


def city_calculator(city_count, bonus):
    if bonus:
        return 0.95 * (50000 * (city_count - 1)**3 + 150000*city_count + 75000)
    return 50000 * (city_count - 1)**3 + 150000*city_count + 75000