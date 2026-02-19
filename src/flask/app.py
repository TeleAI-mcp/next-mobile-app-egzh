# This file contains the Flask application class and related logic.
# It is part of the Flask web framework.

import os
import sys
from typing import Any, Callable, Optional, Union


class Flask:
    """The Flask class implements a WSGI application and acts as the central
    object.  Once it is created it will act as a central registry for
    the view functions, the URL rules, template configuration and much more.

    The name of the package is used to resolve resources from inside the
    package or the folder the module is contained in depending on if the
    package parameter resolves to an actual python package (a folder with
    an :file:`__init__.py` file inside) or a standard module (just a ``.py`` file).

    For more information about resource loading, see :func:`open_resource`.

    Usually you create a :class:`Flask` instance in your main module or
    in the :file:`__init__.py` file of your package like this::

        from flask import Flask
        app = Flask(__name__)

    .. admonition:: About the First Parameter

        The idea of the first parameter is to give Flask an idea of what
        belongs to your application.  This name is used to find resources
        on the filesystem, can be used by extensions to improve debugging
        information and a lot more.

        So it's important what you provide there.  If you are using a single
        module, `__name__` is always the correct value.  If you however are
        using a package, it's usually recommended to hardcode the name of
        your package there.

        For example if your application is defined in :file:`yourapplication/app.py`
        you should create it with one of the two values below::

            app = Flask('yourapplication')
            app = Flask(__name__.split('.')[0])

        Why is that?  The application will work even with `__name__`, thanks
        to how resources are looked up.  However it will make debugging more
        painful.  Certain extensions can make assumptions based on the import
        name of your application.  For example the Flask-SQLAlchemy extension
        will look for the code in your application that triggered an SQL query
        in `__name__` is not set properly.

    .. versionadded:: 0.7
       The `static_url_path`, `static_folder`, and `template_folder`
       parameters were added.

    .. versionadded:: 0.8
       The `instance_relative_config` parameter was added.

    .. versionadded:: 1.0
       The `host_matching` and `static_host` parameters were added.

    .. versionadded:: 1.0
       The `subdomain_matching` parameter was added.  Subdomain
       matching needs to be enabled in :data:`SERVER_NAME` setting as well.

    .. versionadded:: 1.0
       The `propagate_exceptions` parameter was added.

    .. versionchanged:: 1.0
       `debug` parameter does nothing anymore.

    .. versionadded:: 1.1
       The `root_path` parameter was added.

    .. versionchanged:: 1.1
       The `instance_path` parameter was deprecated.
    """

    def __init__(
        self,
        import_name: str,
        static_url_path: Optional[str] = None,
        static_folder: Optional[str] = "static",
        static_host: Optional[str] = None,
        host_matching: bool = False,
        subdomain_matching: bool = False,
        template_folder: Optional[str] = "templates",
        instance_path: Optional[str] = None,
        instance_relative_config: bool = False,
        root_path: Optional[str] = None,
    ) -> None:
        """Initialize the Flask application."""
        self.import_name = import_name
        self.static_url_path = static_url_path
        self.static_folder = static_folder
        self.static_host = static_host
        self.host_matching = host_matching
        self.subdomain_matching = subdomain_matching
        self.template_folder = template_folder
        self.instance_path = instance_path
        self.instance_relative_config = instance_relative_config
        self.root_path = root_path

    def run(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        debug: Optional[bool] = None,
        load_dotenv: bool = True,
        **options: Any,
    ) -> None:
        """Runs the application on a local development server."""
        pass

    def route(self, rule: str, **options: Any) -> Callable:
        """A decorator that is used to register a view function for a
        given URL rule.  This does the same thing as :meth:`add_url_rule`
        but is intended for decorator usage::

            @app.route('/')
            def index():
                return 'Hello World'

        :param rule: the URL rule as string
        :param endpoint: the endpoint for the registered URL rule.  Flask
                         itself assumes the name of the view function as
                         endpoint
        :param options: the options to be forwarded to the underlying
                        :class:`~werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options.  methods
                        is a list of methods this rule should be limited
                        to (``GET``, ``POST`` etc.).  By default a rule
                        just listens for ``GET`` (and implicitly ``HEAD``).
        """
        def decorator(f: Callable) -> Callable:
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator

    def add_url_rule(
        self,
        rule: str,
        endpoint: Optional[str] = None,
        view_func: Optional[Callable] = None,
        **options: Any,
    ) -> None:
        """Connects a URL rule.  Works exactly like the :meth:`route`
        decorator.  If a view_func is provided it will be registered with the
        endpoint.

        Basically this example::

            @app.route('/')
            def index():
                return 'Hello World'

        Is equivalent to the following::

            def index():
                return 'Hello World'
            app.add_url_rule('/', 'index', index)

        :param rule: the URL rule as string
        :param endpoint: the endpoint for the registered URL rule.  Flask
                         itself assumes the name of the view function as
                         endpoint
        :param view_func: the function to call when serving a request to the
                          provided endpoint
        :param options: the options to be forwarded to the underlying
                        :class:`~werkzeug.routing.Rule` object
        """
        pass
