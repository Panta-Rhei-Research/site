---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_germ_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/spectral-germ-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::spectral_germ_check",
  "declaration_slug": "spectral-germ-check",
  "kind": "def",
  "name": "spectral_germ_check",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 217,
  "source_line_end": 218,
  "registry_ids": [
    "II.L03"
  ],
  "related_registry_items": [
    {
      "id": "II.L03",
      "title": "Spectral-Germ Equivalence",
      "url": "/registry/object/II.L03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L217-L218",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.MutualDetermination",
        "url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L217-L218",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Hartogs.MutualDetermination](/verify/taulib/docs/book-ii-hartogs-mutual-determination/)
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L217-L218)
- Source range: L217-L218
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L03` — Spectral-Germ Equivalence

## Immediate Comment / Docstring

```lean
/-- [II.L03] Spectral <-> Omega-germ:
    Spectral stability implies germ equivalence. If the spectral
    decomposition at each stage is determined by the reduction map,
    then the profinite limit (omega-germ) is determined. -/
```

## Source Excerpt

```lean
def spectral_germ_check (bound db : TauIdx) : Bool :=
  spectral_tail_check bound db && omega_germ_check bound db
```
