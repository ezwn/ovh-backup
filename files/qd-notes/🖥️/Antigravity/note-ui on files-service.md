The goal is to completely rebase the note feature, which currently includes note-ui docurests and a data backend on files-service.

It means that the current backend of the note feature would be replaced by files-service.

To implement this, files-service would be started only once (for serving both notes-ui and quickcms) and a specific folder would be were we store the notes.

One problem we have to find a solution to is the publishing of notes,  which is currently done through note-ui eyes backend.

Now please assess this migration : what will we lose in the process? Is it feasible? Ask me for features that we don't need anymore once you listed them.

---