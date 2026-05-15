---
{
  "projection_kind": "taulib_declaration",
  "title": "projector_check",
  "permalink": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/projector-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::projector_check",
  "declaration_slug": "projector-check",
  "kind": "def",
  "name": "projector_check",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 111,
  "source_line_end": 112,
  "registry_ids": [
    "III.D80"
  ],
  "related_registry_items": [
    {
      "id": "III.D80",
      "title": "q-Expansion Coefficients",
      "url": "/registry/object/III.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L111-L112",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralDecomp",
        "url": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L111-L112",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Doors.SpectralDecomp](/corpus/taulib/docs/book-iii-doors-spectral-decomp/)
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L111-L112)
- Source range: L111-L112
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D80` — q-Expansion Coefficients

## Immediate Comment / Docstring

```lean
/-- [III.D80] Full projector check: idempotent + orthogonal. -/
```

## Source Excerpt

```lean
def projector_check (N : Nat) : Bool :=
  projector_idempotent_check N && projector_orthogonal_check N
```
