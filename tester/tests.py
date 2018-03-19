from django.test import TestCase
from django import forms
from django.urls import reverse
from .models import ColourCombo

class ViewTests(TestCase):

    def test_combo_list(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")
        c1 = ColourCombo.objects.create(
            bgcolour_one="#a1a1a3", bgcolour_two="#f4f4f4", 
            textcolour_one="#efefef", textcolour_two="#abcdef")

        response = self.client.get(reverse("index"))

        self.assertEqual(ColourCombo.objects.count(), 2)
        self.assertTemplateUsed(response, "tester/index.html")

        # check text colours displayed for each combo
        self.assertContains(response, "000000")
        self.assertContains(response, "f4f4f4")
        self.assertContains(response, "c9e5a2")
        self.assertContains(response, "abcdef")

    def test_add_combo_intial(self):
        response = self.client.get(reverse("add_combo"))
        self.assertTemplateUsed(response, "tester/combo.html")

        # contains default colours
        self.assertContains(response, "#FF5733")
        self.assertContains(response, "E58571")
        self.assertContains(response, "000000")

    def test_edit_combo_initial(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        self.assertContains(response, "ffffff")
        self.assertContains(response, "000000")
        self.assertContains(response, "efefef")
        self.assertContains(response, "c9e5a2")

    def test_adding_a_combo_success(self):
        response = self.client.get(reverse("add_combo"))
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertEqual(ColourCombo.objects.count(), 0)

        response = self.client.post(
            reverse("add_combo"),
            data = {
                "save-button": "save",
                "bgcolour_one": "#ffffff", 
                "bgcolour_two": "#000000", 
                "textcolour_one": "#efefef", 
                "textcolour_two": "#c9e5a2"
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tester/index.html")
        self.assertEqual(ColourCombo.objects.count(), 1)

    def test_edit_a_combo_success(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["textcolour_one"] = "#444444"
        data["save-button"] = "save"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tester/index.html")
        self.assertNotContains(response, "#efefef")
        self.assertContains(response, "#444444")

    def test_delete_combo(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["delete-button"] = "delete"

        self.assertEqual(ColourCombo.objects.count(), 1)
        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tester/index.html")
        self.assertEqual(ColourCombo.objects.count(), 0)

    def test_apply_combo_failure_invalid_background1(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["bgcolour_one"] = "#44444"
        data["apply-button"] = "apply"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid background colour")

    def test_apply_combo_failure_invalid_background2(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["bgcolour_two"] = "#44444"
        data["apply-button"] = "apply"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid background colour")

    def test_apply_combo_failure_invalid_textcolour1(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["textcolour_one"] = "#44444"
        data["apply-button"] = "apply"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid text colour")

    def test_apply_combo_failure_invalid_textcolour2(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["textcolour_two"] = "#44444"
        data["apply-button"] = "apply"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid text colour")

    def test_adding_combo_failure_invalid_background1(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["bgcolour_one"] = "#44444"
        data["save-button"] = "save"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid background colour")

    def test_adding_combo_failure_invalid_background2(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["bgcolour_two"] = "#44444"
        data["save-button"] = "save"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid background colour")

    def test_adding_combo_failure_invalid_textcolour1(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["textcolour_one"] = "#44444"
        data["save-button"] = "save"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid text colour")

    def test_adding_combo_failure_invalid_textcolour2(self):
        c1 = ColourCombo.objects.create(
            bgcolour_one="#ffffff", bgcolour_two="#000000", 
            textcolour_one="#efefef", textcolour_two="#c9e5a2")

        response = self.client.get(reverse("edit_combo", 
                                   kwargs={"combo_id": c1.pk}))
        self.assertTemplateUsed(response, "tester/combo.html")

        form = response.context['form']
        data = form.initial
        data["textcolour_two"] = "#44444"
        data["save-button"] = "save"

        response = self.client.post(
            reverse('edit_combo', kwargs={"combo_id": c1.pk}),
            data,
            follow = True
        )
        self.assertTemplateUsed(response, "tester/combo.html")
        self.assertContains(response, "Invalid text colour")