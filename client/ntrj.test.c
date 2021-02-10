/*
 * This small test has been created for trying to open a picture in C. 
 *
 * As this is a learning proyect, sometimes I have to create this small 
 * files that contain examples of basic things.
 *
 * For more information: github.com/pblcc/trj
 *
 * Follow me on Twitter: @pablocorbcon
 *
 * To compile this test use:
 *
 *   gcc -Wall ntrj.test.c -o ntrj.test `pkg-config --cflags --libs gtk+-3.0`
 */
#include <gtk/gtk.h>

void destroy(void) 
{
  gtk_main_quit();
}

int main(int argc, char** argv)
{
  GtkWidget* window;
  GtkWidget* image;

  gtk_init(&argc, &argv);

  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
  image = gtk_image_new_from_file(argv[1]);

  gtk_signal_connect(GTK_OBJECT (window), "destroy", GTK_SIGNAL_FUNC(destroy), NULL);

  gtk_container_add(GKT_CONTAINER (window), image);
  gtk_widget_show_all(window);
  gtk_main();
  return 0;
}
