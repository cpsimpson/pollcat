from django.contrib import admin
from ballots.models import Poll, Category, CategoryItem, Ballot, Vote, Answer, AnswerItem


# class ItemInline(admin.TabularInline):
#     model = CategoryItem
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [ItemInline,
#                ]


class CategoryInline(admin.TabularInline):
    model = Category


class PollAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,
               ]


class VoteInline(admin.TabularInline):
    model = Vote


class BallotAdmin(admin.ModelAdmin):
    inlines = [VoteInline,
               ]

admin.site.register(Poll, PollAdmin)
admin.site.register(Category)
admin.site.register(CategoryItem)
admin.site.register(Ballot, BallotAdmin)
admin.site.register(Vote)
admin.site.register(Answer)
admin.site.register(AnswerItem)