from Backstage import db, fsqla


class Role(db.Model, fsqla.FsRoleMixin):

    def __str__(self):
        return self.name


class User(db.Model, fsqla.FsUserMixin):

    def __str__(self):
        return self.email

