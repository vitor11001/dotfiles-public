use inquire::Select;
use crate::modules::exit::{ExitChoices, close_program};
use crate::constants::packages::{PIPEWIRE_PACKAGES, PULSEAUDIO_PACKAGES};
use crate::installations::install_from_pacman::install_from_pacman;


pub fn choice_audio_packages() {
    let audio_packages = vec![
        "Pulseaudio packages",
        "Pipewire packages",
        "exit"
    ];

    let audio_packages_ans = Select::new(
        "Which audio packages would you like to install?", 
        audio_packages
    ).prompt();

    if let Ok(choice) = audio_packages_ans {
        match choice {
            "Pulseaudio packages" => install_from_pacman(PULSEAUDIO_PACKAGES, "pulseaudio packages"),
            "Pipewire packages" => install_from_pacman(PIPEWIRE_PACKAGES, "pipewire packages"),
            "exit" => close_program(ExitChoices::Exit),
            _ => close_program(ExitChoices::InvalidChoice),
        }
    } else {
        close_program(ExitChoices::Error);
    }
}
