class ReactAppViewMixin(object):
    component = None

    def get_context_data(self, **kwargs):
        context = super(ReactAppViewMixin, self).get_context_data(**kwargs)
        context['component'] = self.component

        return context
