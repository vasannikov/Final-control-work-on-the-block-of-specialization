from registry import Registry, main_menu
from counter import Counter, add_new_animal_with_counter

if __name__ == "__main__":
    registry = Registry()

    with Counter() as counter:
        add_new_animal_with_counter(registry, counter)
        add_new_animal_with_counter(registry, counter)
        print(f"Total animals added: {counter.get_count()}")

    main_menu(registry)