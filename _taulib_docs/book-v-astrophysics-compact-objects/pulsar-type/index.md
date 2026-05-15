---
{
  "projection_kind": "taulib_declaration",
  "title": "PulsarType",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-compact-objects/pulsar-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::PulsarType",
  "declaration_slug": "pulsar-type",
  "kind": "inductive",
  "name": "PulsarType",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 152,
  "source_line_end": 159,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L152-L159",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.CompactObjects",
        "url": "/corpus/taulib/docs/book-v-astrophysics-compact-objects/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L152-L159",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookV.Astrophysics.CompactObjects](/corpus/taulib/docs/book-v-astrophysics-compact-objects/)
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L152-L159)
- Source range: L152-L159
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pulsar type. -/
```

## Source Excerpt

```lean
inductive PulsarType where
  /-- Normal pulsar (period 0.1-10 seconds). -/
  | Normal
  /-- Millisecond pulsar (period < 30 ms). -/
  | Millisecond
  /-- Magnetar (B > 10^14 Gauss). -/
  | Magnetar
  deriving Repr, DecidableEq, BEq
```
