---
{
  "projection_kind": "taulib_declaration",
  "title": "mutual_determination_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/mutual-determination-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::mutual_determination_check",
  "declaration_slug": "mutual-determination-check",
  "kind": "def",
  "name": "mutual_determination_check",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 252,
  "source_line_end": 257,
  "registry_ids": [
    "II.T27"
  ],
  "related_registry_items": [
    {
      "id": "II.T27",
      "title": "Mutual Determination (5-Way Equivalence)",
      "url": "/registry/object/II.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L252-L257",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L252-L257",
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
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L252-L257)
- Source range: L252-L257
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T27` — Mutual Determination (5-Way Equivalence)

## Immediate Comment / Docstring

```lean
/-- [II.T27] The Mutual Determination Theorem:
    All five descriptions of holomorphic data at a point agree.

    (R) Refinement tail <-> (S) Spectral tail <-> (G) Omega-germ
    <-> (C) Boundary character <-> (H) Hartogs continuation

    The equivalence chain is:
    - L02: (R) <-> (S)   [refinement coherence = spectral stability]
    - L03: (S) <-> (G)   [spectral stability = germ equivalence]
    - L04: (G) <-> (C)   [germ data = character data]
    - L05: (C) <-> (H)   [character data = Hartogs extension]

    The mechanism: the bipolar idempotent decomposition e_plus, e_minus
    ensures that the B-channel and C-channel carry independent, complete
    information (orthogonality + partition of unity). -/
```

## Source Excerpt

```lean
def mutual_determination_check (bound db : TauIdx) : Bool :=
  refinement_tail_check bound db &&
  spectral_tail_check bound db &&
  omega_germ_check bound db &&
  boundary_character_check bound db &&
  hartogs_check bound db
```
