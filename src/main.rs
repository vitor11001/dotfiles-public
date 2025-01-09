mod constants;
mod modules;
mod installations;

use modules::{
    base_packages::base_packages,
    nvidia_drivers::nvidia_drivers,
    audio_packages::choice_audio_packages,
    bluetooth_packages::bluetooth_packages,
    choices_twm::choices_twm,
};


fn main() {
    base_packages();
    nvidia_drivers();
    choice_audio_packages();
    bluetooth_packages();
    choices_twm();
}
