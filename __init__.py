from mycroft import MycroftSkill, intent_file_handler


class PlexDirector(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('director.plex.intent')
    def handle_director_plex(self, message):
        movie = message.data.get('movie')
        song = message.data.get('song')

        self.speak_dialog('director.plex', data={
            'movie': movie,
            'song': song
        })


def create_skill():
    return PlexDirector()

