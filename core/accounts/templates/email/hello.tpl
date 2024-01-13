{% extends "mail_templated/base.tpl" %}

{% block subject %}
Email
{% endblock %}

{% block body %}
This is a plain text part.
{% endblock %}

{% block html %}
{{token}}
{% endblock %}