class MicrowaveOpen(Kitchen):
    def __init__(self, *args, **kwargs):
        print("init log")
        super().__init__(*args, **kwargs)

    def _setup_kitchen_references(self):
        super()._setup_kitchen_references()
        
        self.microwave = self.register_fixture_ref("microwave", dict(id=FixtureType.MICROWAVE))
        self.init_robot_base_pos = self.microwave 

    def get_ep_meta(self):
        ep_meta = super().get_ep_meta()
        ep_meta["lang"] = f"Open the microwave door."
        
        return ep_meta
    
    def _reset_internal(self):
        super()._reset_internal()
        self.microwave.set_door_state(min=0, max=0, env=self, rng=self.rng) # TODO: check if that is a closed door

    def _get_obj_cfgs(self):
        # no items or distractors needed
        cfgs = []
        return cfgs
    
    def _check_success(self):
        door_state = self.microwave.get_door_state(env=self)
        door_opened = False

        for joint_p in door_state.values():
            if joint_p > 0.1: # TODO: check if that is the correcht joint value
                door_opened = True
                break
        
        return door_opened
