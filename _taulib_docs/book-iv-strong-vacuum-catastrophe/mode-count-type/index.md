---
{
  "projection_kind": "taulib_declaration",
  "title": "ModeCountType",
  "permalink": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/mode-count-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::ModeCountType",
  "declaration_slug": "mode-count-type",
  "kind": "inductive",
  "name": "ModeCountType",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 133,
  "source_line_end": 138,
  "registry_ids": [
    "IV.D193"
  ],
  "related_registry_items": [
    {
      "id": "IV.D193",
      "title": "Earned vs.\\ unearned mode count",
      "url": "/registry/object/IV.D193/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L133-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.VacuumCatastrophe",
        "url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L133-L138",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "status": "defined"
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

- Module: [TauLib.BookIV.Strong.VacuumCatastrophe](/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/)
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L133-L138)
- Source range: L133-L138
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D193` — Earned vs.\ unearned mode count

## Immediate Comment / Docstring

```lean
/-- [IV.D193] Mode count classification:

    EARNED: N_n = dim(H_partial[n]|_{T^2}) < infinity,
    the number of independent boundary characters on T^2 at stage n.
    Finite at every stage, grows with n, profinite limit is well-defined.

    UNEARNED: any infinite cardinal assigned to continuum field theory
    modes a priori, without derivation from a finite construction.
    This is the source of the vacuum catastrophe in orthodox QFT. -/
```

## Source Excerpt

```lean
inductive ModeCountType where
  /-- Earned: finite at each stage, profinite limit. -/
  | earned
  /-- Unearned: infinite cardinal assigned a priori. -/
  | unearned
  deriving Repr, DecidableEq, BEq
```
