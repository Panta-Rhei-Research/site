---
{
  "projection_kind": "taulib_declaration",
  "title": "liouville_dodge_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/liouville-dodge-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::liouville_dodge_check",
  "declaration_slug": "liouville-dodge-check",
  "kind": "def",
  "name": "liouville_dodge_check",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 60,
  "source_line_end": 79,
  "registry_ids": [
    "II.T41"
  ],
  "related_registry_items": [
    {
      "id": "II.T41",
      "title": "Liouville Categorical Dodge",
      "url": "/registry/object/II.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L60-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L60-L79",
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

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L60-L79)
- Source range: L60-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T41` — Liouville Categorical Dodge

## Immediate Comment / Docstring

```lean
/-- [II.T41] Liouville dodge check: verify that j^2 = +1 (split-complex,
    NOT complex) and that this gives wave-type (hyperbolic) structure,
    not elliptic.

    j^2 = +1 means: SplitComplex.mul j j = SplitComplex.one.
    This is the wave-type condition: the "Laplacian" is
    box = d^2/dx^2 - d^2/dy^2 (two opposite signs),
    not Delta = d^2/dx^2 + d^2/dy^2 (two same signs).

    In sector coordinates: e_plus * e_minus = 0 (zero divisors exist).
    This is IMPOSSIBLE in the complex case (i^2 = -1 has no nontrivial
    idempotents over Z). -/
```

## Source Excerpt

```lean
def liouville_dodge_check : Bool :=
  -- j^2 = +1 (wave type)
  let j_sq := SplitComplex.mul SplitComplex.j SplitComplex.j
  let wave_ok := j_sq == SplitComplex.one
  -- Zero divisors exist: e_plus * e_minus = 0
  let zd := SectorPair.mul e_plus_sector e_minus_sector
  let zd_ok := zd == (SectorPair.mk 0 0)
  -- e_plus and e_minus are nontrivial (not zero, not one)
  let ep_nontrivial := e_plus_sector != (SectorPair.mk 0 0) &&
                        e_plus_sector != (SectorPair.mk 1 1)
  let em_nontrivial := e_minus_sector != (SectorPair.mk 0 0) &&
                        e_minus_sector != (SectorPair.mk 1 1)
  -- Idempotency: e^2 = e
  let ep_idem := SectorPair.mul e_plus_sector e_plus_sector == e_plus_sector
  let em_idem := SectorPair.mul e_minus_sector e_minus_sector == e_minus_sector
  -- Completeness: e_plus + e_minus = 1
  let complete := SectorPair.add e_plus_sector e_minus_sector ==
                  (SectorPair.mk 1 1)
  wave_ok && zd_ok && ep_nontrivial && em_nontrivial &&
  ep_idem && em_idem && complete
```
