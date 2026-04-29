---
{
  "projection_kind": "taulib_declaration",
  "title": "idempotent_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/idempotent-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.JReplacesI`.",
  "declaration_id": "TauLib.BookII.Transcendentals.JReplacesI::idempotent_check",
  "declaration_slug": "idempotent-check",
  "kind": "def",
  "name": "idempotent_check",
  "module_name": "TauLib.BookII.Transcendentals.JReplacesI",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/",
  "source_line_start": 67,
  "source_line_end": 75,
  "registry_ids": [
    "II.D33"
  ],
  "related_registry_items": [
    {
      "id": "II.D33",
      "title": "Bipolar Idempotents Interior",
      "url": "/registry/object/II.D33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L67-L75",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.JReplacesI",
        "url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L67-L75",
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

- Module: [TauLib.BookII.Transcendentals.JReplacesI](/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/)
- Source path: [`TauLib/BookII/Transcendentals/JReplacesI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L67-L75)
- Source range: L67-L75
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D33` — Bipolar Idempotents Interior

## Immediate Comment / Docstring

```lean
/-- [II.D33] Bipolar idempotents in sector coordinates.
    e_+ = (1, 0) and e_- = (0, 1) in SectorPair.

    Algebraic properties:
    1. e_+^2 = e_+ (idempotent)
    2. e_-^2 = e_- (idempotent)
    3. e_+ * e_- = 0 (orthogonal)
    4. e_+ + e_- = (1,1) = unity -/
```

## Source Excerpt

```lean
def idempotent_check : Bool :=
  -- e_+ idempotent
  SectorPair.mul e_plus_sector e_plus_sector == e_plus_sector &&
  -- e_- idempotent
  SectorPair.mul e_minus_sector e_minus_sector == e_minus_sector &&
  -- Orthogonality
  SectorPair.mul e_plus_sector e_minus_sector == ⟨0, 0⟩ &&
  -- Partition of unity
  SectorPair.add e_plus_sector e_minus_sector == ⟨1, 1⟩
```
