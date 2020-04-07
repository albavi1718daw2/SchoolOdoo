# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teacher(models.Model):
  _name = 'school.teacher'
  _description = 'Teacher Management'
  _rec_name = 'last_name'

  first_name = fields.Char('First Name',size=30,required=True)
  last_name = fields.Char('Last Name',size=40,required=True)
  birthdate = fields.Date('Birthdate',required=True)
  tin = fields.Char('Tax ID',size=14,required=True)
  gender = fields.Selection([('male','Male'),('female','Female')],'Gender')
  salary = fields.Integer('Salary')
  email = fields.Char('eMail',size=60,required=True)
  phone = fields.Char('Phone')
  active = fields.Boolean('Active?',default=True)
  course_ids = fields.One2many('school.course','manager_id','Courses managed',
                               readonly=True)
  subject_ids = fields.Many2many('school.subject','school_subject_teacher_rel','teacher_id','subject_id',
                                 'Subjects authorized',readonly=True)
  country_id = fields.Many2one('school.country','Country Manager')

class Course(models.Model):
  _name = 'school.course'
  _description = 'Course Management'
  
  name = fields.Char('Name',size=60,required=True)
  hours = fields.Integer('Hours',required=True)
  active = fields.Boolean('Active?',default=True)
  manager_id = fields.Many2one('school.teacher','Teacher Manager')
  subject_ids = fields.Many2many('school.subject','school_course_subject_rel',
                                 'course_id','subject_id','Subjects')

class Subject(models.Model):
  _name = 'school.subject'
  _description = 'Subject Management'
  
  name = fields.Char('Name',size=60,required=True)
  hours = fields.Integer('Hours',required=True)
  active = fields.Boolean('Active?',default=True)
  course_ids = fields.Many2many('school.course','school_course_subject_rel',
                                'subject_id','course_id','Courses')
  teacher_ids = fields.Many2many('school.teacher','school_subject_teacher_rel','subject_id','teacher_id',
                                 'Authorized Teachers',readonly=True)

class Country(models.Model):
  _name = 'school.country'
  _description = 'Country Management'

  name = fields.Char('Name',size=60,required=True)
  teacher_ids = fields.One2many('school.teacher','country_id','Teachers managed',
                                 readonly=True)

