---
{
  "projection_kind": "taulib_declaration",
  "title": "presheaf_restrict",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/presheaf-restrict/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::presheaf_restrict",
  "declaration_slug": "presheaf-restrict",
  "kind": "def",
  "name": "presheaf_restrict",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 99,
  "source_line_end": 100,
  "registry_ids": [
    "II.D47"
  ],
  "related_registry_items": [
    {
      "id": "II.D47",
      "title": "Holomorphic Presheaf",
      "url": "/registry/object/II.D47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L99-L100",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L99-L100",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L99-L100)
- Source range: L99-L100
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D47` — Holomorphic Presheaf

## Immediate Comment / Docstring

```lean
/-- [II.D47] Presheaf restriction map: from cylinder at stage l to
    cylinder at stage k (for k ≤ l).

    The restriction of a value a at stage l to stage k is reduce(a, k).
    This is the canonical projection Z/P_lZ → Z/P_kZ. -/
```

## Source Excerpt

```lean
def presheaf_restrict (a l k : TauIdx) : TauIdx :=
  if k ≤ l then reduce a k else a
```
