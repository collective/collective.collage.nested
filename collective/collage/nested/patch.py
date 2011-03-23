patched_collage_types = lambda: ('CollageRow', 'CollageColumn', 'CollageAlias')

def apply_collage_types_patch(scope, original, replacement):
    setattr(scope, original, replacement())
    return

#def collage_types():
#    from Products.Collage import config
#    config.COLLAGE_TYPES = ('CollageRow', 'CollageColumn', 'CollageAlias')
#    log.info('Monkey patching Products.Collage.config (COLLAGE_TYPES)')

def enabledType(self, portal_type):
    if portal_type == 'Collage':
        return True
    else:
        return self._old_enabledType(portal_type)

def enabledAlias(self, portal_type):
    if portal_type == 'Collage':
        return True
    else:
        return self._old_enabledAlias(portal_type)


