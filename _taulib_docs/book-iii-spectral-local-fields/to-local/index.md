---
{
  "projection_kind": "taulib_declaration",
  "title": "to_local",
  "permalink": "/verify/taulib/docs/book-iii-spectral-local-fields/to-local/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::to_local",
  "declaration_slug": "to-local",
  "kind": "def",
  "name": "to_local",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/verify/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 43,
  "source_line_end": 45,
  "registry_ids": [
    "III.D21"
  ],
  "related_registry_items": [
    {
      "id": "III.D21",
      "title": "τ-Native Local Field",
      "url": "/registry/object/III.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L43-L45",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.LocalFields",
        "url": "/verify/taulib/docs/book-iii-spectral-local-fields/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L43-L45",
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

- Module: [TauLib.BookIII.Spectral.LocalFields](/verify/taulib/docs/book-iii-spectral-local-fields/)
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L43-L45)
- Source range: L43-L45
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D21` — τ-Native Local Field

## Immediate Comment / Docstring

```lean
/-- [III.D21] Build a local field element from a global τ-value. -/
```

## Source Excerpt

```lean
def to_local (x p d : TauIdx) : LocalFieldElt :=
  let pd := p ^ d
  ⟨p, d, if pd > 0 then x % pd else 0⟩
```
