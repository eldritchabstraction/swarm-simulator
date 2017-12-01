# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import json

# Create your models here.

class Controller(models.Model):
    def buy(self, creature, quantity):
        # check resources

        # check buy max

