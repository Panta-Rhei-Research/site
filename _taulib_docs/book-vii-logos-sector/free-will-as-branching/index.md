---
{
  "projection_kind": "taulib_declaration",
  "title": "free_will_as_branching",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/free-will-as-branching/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::free_will_as_branching",
  "declaration_slug": "free-will-as-branching",
  "kind": "theorem",
  "name": "free_will_as_branching",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 236,
  "source_line_end": 239,
  "registry_ids": [
    "VII.T43"
  ],
  "related_registry_items": [
    {
      "id": "VII.T43",
      "title": "Free Will as Branching",
      "url": "/registry/object/VII.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L236-L239",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L236-L239",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L236-L239)
- Source range: L236-L239
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T43` — Free Will as Branching

## Immediate Comment / Docstring

```lean
/-- [VII.T43] Free Will as Branching (ch113). Free will modelled as
    branching in the temporal category: at decision points, multiple
    admissible continuations exist. Choice = selection of a branch.
    Determinism-indeterminism is scale-dependent (VII.T23). -/
```

## Source Excerpt

```lean
theorem free_will_as_branching :
    mind_topos.has_exponentials = true ∧
    mind_topos.has_internal_logic = true :=
  ⟨rfl, rfl⟩
```
