import fresh_tomatoes
from media import *


# the main function of the program
def main():
    movies = create_movies_list()
    series = create_tv_shows_list()

    # appending the two generated lists
    movies = movies + series

    # This function call opens a page of movies generated
    # by the create_movies_list() and create_tvshows_list() methods
    fresh_tomatoes.open_movies_page(movies)


def create_movies_list():
    godfather = Movie('The Godfather',
                      '''\
                       The aging patriarch of an organized crime dynasty
                       transfers control of his clandestine empire to his reluctant son.''',
                      'https://www.youtube.com/watch?v=sY1S34973zA',
                      'http://img.zanda.com/item/57040290000061/730xauto/The_Godfather.jpg',
                      '24 March 1972 (USA)', 'Crime, Drama', ' 2h 55min', rating=Movie.RATINGS[3]
                      )

    mystic_river = Movie('Mystic River',
                         '''\
                         three men are reunited by circumstance when one has a family tragedy''',
                         'https://www.youtube.com/watch?v=W7NktJhrRYQ',
                         'https://encrypted-tbn0.gstatic.com/images?q=tbn:' \
                         + 'ANd9GcQYSMiwLB3Bdc2TG5PC2Gacv3CEFMlH2UeZtDvESUonATbBdm0J',
                         ' 15 October 2003 (USA)', 'Drama, Mystery', '2h 18min', rating=Movie.RATINGS[3])

    pulp_fiction = Movie('Pulp Fiction',
                         '''\
                        Two mob hit men, a boxer,
                        a gangster's wife, and a pair of bandits intertwine in four tales of violence and redemption.''',
                         'https://www.youtube.com/watch?v=s7EdQ4FqbhY',
                         'https://ih0.redbubble.net/image.57066806.8556/flat,800x800,075,f.u4.jpg',
                         '14 October 1994 (USA)', ' Crime, Drama', '2h 34min', rating=Movie.RATINGS[3])

    b_mind = Movie('A Beautiful Mind', '''\
                                         After John Nash, a brilliant but asocial mathematician,
                                         accepts secret work in cryptography, his life takes a turn for the nightmarish.''',
                   'https://www.youtube.com/watch?v=aS_d0Ayjw4o',
                   'https://images-na.ssl-images-amazon.com/images/M/MV5BMzcwYWFkYzktZjAzNC00OGY1LWI4YTgtNzc' \
                   + '5MzVjMDVmNjY0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,673,1000_AL_.jpg',
                   '4 January 2002 (USA)', ' Biography, Drama', '2h 15min', rating=Movie.RATINGS[2])

    dead_poets_society = Movie('Dead Poets Society', '''\
                                English teacher John Keating inspires his students to look at poetry with
                                 a different perspective of authentic knowledge and feelings.''',
                               'https://www.youtube.com/watch?v=4lj185DaZ_o',
                               'https://images-na.ssl-images-amazon.com/images/M/MV5BOGYwYWNjMzgtNGU4ZC00NWQ2LWEwZjUt' \
                               + 'MzE1Zjc3NjY3YTU1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,677,1000_AL_.jpg',
                               '9 June 1989 (USA)', 'Comedy, Drama', '2h 8min', rating=Movie.RATINGS[2])

    king_sp = Movie('The King\'s Speech', '''\
                    The story of King George VI of the United Kingdom of Great Britain and Northern Ireland.''',
                    'https://www.youtube.com/watch?v=kYoSQkfrjfA',
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BMzU5MjEwMTg2Nl5' \
                    + 'BMl5BanBnXkFtZTcwNzM3MTYxNA@@._V1_SY1000_CR0,0,684,1000_AL_.jpg',
                    '25 December 2010 (USA)', 'Biography, Drama', ' 1h 58min', rating=Movie.RATINGS[3])

    schindler = Movie('Schindler\'s List', '''\
                             Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their
                              persecution by the Nazi''',
                      'https://www.youtube.com/watch?v=gG22XNhtnoY',
                      'https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy0' \
                      + '0NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
                      '4 February 1994 (USA)', ' Biography, Drama, History', '3h 15min', rating=Movie.RATINGS[3])

    amadeus = Movie('Amadeus', '''\
                               The incredible story of Wolfgang Amadeus Mozart,
                                told by his peer and secret rival Antonio Salieri.
                               ''',
                    'https://www.youtube.com/watch?v=r7kWQj9FCGY',
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTg5NDkwM' \
                    + 'Tk5N15BMl5BanBnXkFtZTYwODg3MDk2._V1_.jpg',
                    '19 September 1984', 'Biography, Drama, History', '2h 40min', rating=Movie.RATINGS[2])

    full_metal = Movie('Full Metal Jacket', '''\
                            A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow recruits.
                               ''',
                       'https://www.youtube.com/watch?v=x9f6JaaX7Wg',
                       'https://images-na.ssl-images-amazon.com/images/M/MV5BNzc2ZThkOGItZGY5' \
                       + 'YS00MDYwLTkyOTAtNDRmZWIwMGRhYTc0L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,656,1000_AL_.jpg',
                       '10 July 1987 (USA)', 'Drama, War', '1h 56min', rating=Movie.RATINGS[3])

    clockwork = Movie('A Clockwork Orange', '''\
                                a sadistic gang leader is imprisoned and volunteers for a conduct-aversion experiment,
                                but it doesn't go as planned.
                               ''',
                      'https://www.youtube.com/watch?v=SPRzm8ibDQ8',
                      'https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3MjM1Mzc4N15' \
                      + 'BMl5BanBnXkFtZTgwODM0NzAxMDE@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                      '2 February 1972 (USA)', 'Crime, Drama', '2h 16min', rating=Movie.RATINGS[3])

    c_kane = Movie('Citizen Kane', '''\
                               Following the death of a publishing tycoon,
                                news reporters scramble to discover the meaning of his final utterance.
                               ''',
                   'https://www.youtube.com/watch?v=8dxh3lwdOFw',
                   'https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2' \
                   + 'Mjc1MDQwMl5BMl5BanBnXkFtZTcwNzUyOTUyMg@@._V1_.jpg',
                   '5 September 1941 (USA)', 'Drama', '1h 59min', rating=Movie.RATINGS[2])

    usual_sus = Movie('The Usual Suspects', '''\
                               A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat.
                               ''',
                      'https://www.youtube.com/watch?v=oiXdPolca5w',
                      'https://images-na.ssl-images-amazon.com/images/M/MV5BYTViNjMyNmUtNDFkNC00ZDRlLT' \
                      + 'hmMDUtZDU2YWE4NGI2ZjVmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,670,1000_AL_.jpg',
                      '15 September 1995 (USA)', 'Crime, Drama, Mystery', '1h 46min', rating=Movie.RATINGS[3])

    snatch = Movie('Snatch', '''\
                                the story of boxing promoters, bookmakers, a Russian gangster, incompetent amateur robbers,
                                and Jewish jewelers.
                               ''',
                   'https://www.youtube.com/watch?v=ni4tEtuTccc',
                   'https://images-na.ssl-images-amazon.com/images/M/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTg' \
                   + 'xMTQtMWI1MGI0ZGQ5MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX684_AL_.jpg',
                   '19 January 2001 (USA)', 'Comedy, Crime', '1h 42min', rating=Movie.RATINGS[3])

    movies = [usual_sus, b_mind, dead_poets_society, snatch, mystic_river, full_metal, pulp_fiction,
              king_sp, amadeus, c_kane, clockwork, godfather, schindler]
    return movies


def create_tv_shows_list():
    breaking_bad = TVSeries('Breaking Bad', '''\
                                   A high school chemistry teacher diagnosed with lung cancer turns to cocking
                                    meth in order to secure his family's future.''',
                            'https://www.youtube.com/watch?v=HhesaQXLuRY',
                            'https://images-na.ssl-images-amazon.com/images/M/MV5BZDNhNzhkNDctOTlmOS' \
                            + '00NWNmLWEyODQtNWMxM2UzYmJiNGMyXkEyXkFqcGdeQXVyNTMxMjgxMzA@._V1_.jpg',
                            '(2008 2013)', 'Crime, Drama, Thriller', '5', rating=TVSeries.RATINGS[4])

    rick_morty = TVSeries('Rick And Morty', '''\
                               An animated series that follows the exploits of a super scientist and his not-so-bright grandson.
                               ''',
                          'https://www.youtube.com/watch?v=WNhH00OIPP0',
                          'https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxNDEwNTE0Nl5B' \
                          + 'Ml5BanBnXkFtZTgwMzQ1MTg3MDE@._V1_.jpg',
                          '(2013 )', 'Animation, Adventure, Comedy', '3', rating=TVSeries.RATINGS[4])

    sopranos = TVSeries('The Sopranos', '''\
                               New Jersey mob boss, Tony Soprano, deals with personal and professional'\
                                issues in his home and business life.
                               ''',
                        'https://www.youtube.com/watch?v=wrN2k3qGbVA',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BZGJjYzhjYTYtMDBjYy00OWU1LTg5O' \
                        + 'TYtNmYwOTZmZjE3ZDdhXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,702,1000_AL_.jpg',
                        '(1999)', 'Crime, Drama', '6', rating=TVSeries.RATINGS[5])

    tw_zone = TVSeries('The Twilight Zone ', '''\
                               Ordinary people find themselves in extraordinarily astounding situations,
                               which they each try to solve in a remarkable manner.
                               ''',
                       'https://www.youtube.com/watch?v=jDrjfDRM5rE',
                       'https://images-na.ssl-images-amazon.com/images/M/MV5BMjAwMTQ1MjE3N15BMl5BanBnXkFtZTYwOTA5' \
                       + 'OTg4._V1._CR10,9,236,390_.jpg',
                       '(1959 1964)', 'Fantasy, Horror, Mystery', '5', rating=TVSeries.RATINGS[3])

    monty_python = TVSeries('Monty Python\'s Flying Circus', '''\
                               The original surreal sketch comedy showcase for the Monty Python troupe.
                               ''',
                            'https://www.youtube.com/watch?v=xJNeRCiq75M',
                            'https://images-na.ssl-images-amazon.com/images/M/MV5BNzY1MDE5OTY4Ml5' \
                            + 'BMl5BanBnXkFtZTgwOTAyNTQ1NjE@._V1_.jpg',
                            '(1969 1974)', 'Comedy', '4', rating=TVSeries.RATINGS[4])

    series = [monty_python, breaking_bad, tw_zone, rick_morty, sopranos]
    return series


if __name__ == "__main__": main()
