---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorPair.trMinus",
  "permalink": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/tr-minus/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::SectorPair.trMinus",
  "declaration_slug": "tr-minus",
  "kind": "def",
  "name": "SectorPair.trMinus",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 127,
  "source_line_end": 147,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L127-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
        "url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L127-L147",
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

- Module: [TauLib.BookI.Polarity.SplitComplexCouplingLift](/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/)
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L127-L147)
- Source range: L127-L147
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Signed-difference trace** on `SectorPair` (paper §6.2 Step 2b
    `Tr_-`):

      `Tr_-(z_+ e_+ + z_- e_-) := z_+ - z_-`.

    The σ-anti-invariant counterpart of `Tr_+`; carries the prime
    polarity character `χ` via the chiTilde bridge below. -/
```

## Source Excerpt

```lean
def SectorPair.trMinus (z : SectorPair) : Int :=
  z.b_sector - z.c_sector

@[simp] theorem SectorPair.trPlus_e_plus :
    SectorPair.trPlus e_plus_sector = 1 := rfl

@[simp] theorem SectorPair.trPlus_e_minus :
    SectorPair.trPlus e_minus_sector = 1 := rfl

@[simp] theorem SectorPair.trPlus_partition :
    SectorPair.trPlus (SectorPair.add e_plus_sector e_minus_sector) = 2 := by
  unfold SectorPair.trPlus SectorPair.add e_plus_sector e_minus_sector
  rfl

@[simp] theorem SectorPair.trMinus_e_plus :
    SectorPair.trMinus e_plus_sector = 1 := rfl

@[simp] theorem SectorPair.trMinus_e_minus :
    SectorPair.trMinus e_minus_sector = -1 := by
  unfold SectorPair.trMinus e_minus_sector
  rfl
```
