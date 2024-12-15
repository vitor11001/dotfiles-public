mod constants;
mod modules;
mod installations;

use modules::{
    base_packages::base_packages,
    nvidia_drivers::nvidia_drivers,
    pipewire_packages::pipewire_packages,
    bluetooth_packages::bluetooth_packages,
};


fn main() {
    base_packages();
    nvidia_drivers();
    pipewire_packages();
    bluetooth_packages();
}
