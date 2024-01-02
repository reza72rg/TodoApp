{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block body %}
This is a plain text part.
{% endblock %}

{% block html %}
This is an <strong>html</strong> part.
{% endblock %}