---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrinoless_double_beta_prediction",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/neutrinoless-double-beta-prediction/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::neutrinoless_double_beta_prediction",
  "declaration_slug": "neutrinoless-double-beta-prediction",
  "kind": "def",
  "name": "neutrinoless_double_beta_prediction",
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 212,
  "source_line_end": 217,
  "registry_ids": [
    "IV.R397"
  ],
  "related_registry_items": [
    {
      "id": "IV.R397",
      "title": "0vbb Prediction: must exist; rate proportional to |<m_bb>|^2",
      "url": "/registry/object/IV.R397/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L212-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.MajoranaStructure",
        "url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L212-L217",
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

- Module: [TauLib.BookIV.Electroweak.MajoranaStructure](/verify/taulib/docs/book-iv-electroweak-majorana-structure/)
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L212-L217)
- Source range: L212-L217
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R397` — 0vbb Prediction: must exist; rate proportional to |<m_bb>|^2

## Immediate Comment / Docstring

```lean
/-- [IV.R397] Neutrinoless double beta decay (0νββ) must exist.

    Reasoning:
    1. Neutrinos are Majorana (proved above).
    2. For Majorana neutrinos, the "neutrino" emitted at one vertex of 0νββ
       can be absorbed at the other vertex (same particle, different helicity).
    3. There is no conserved lepton number to forbid this process.
    4. Therefore 0νββ: (A,Z) → (A,Z+2) + 2e⁻ must occur.

    The rate is proportional to |⟨m_ββ⟩|² where:
    ⟨m_ββ⟩ = |∑ᵢ U²_{ei} · mᵢ| (Majorana effective mass)

    Predicted central value (conjectural, naive PMNS):
    ⟨m_ββ⟩ ≈ 19 meV, range [9, 31] meV.
    Consistent with KamLAND-Zen (< 36–156 meV).
    Within LEGEND-1000 reach (~10 meV sensitivity).

    Scope: conjectural (rate proportionality structural; nuclear matrix element M_nucl
    not derived in τ-framework). -/
```

## Source Excerpt

```lean
def neutrinoless_double_beta_prediction : String :=
  "0vbb decay (A,Z) -> (A,Z+2) + 2e^- must exist: neutrinos are Majorana, " ++
  "L is not conserved. Rate proportional to |<m_bb>|^2 where " ++
  "<m_bb> = |sum_i U_ei^2 * m_i|. " ++
  "Predicted: <m_bb> ~ [9, 19, 31] meV (conjectural, naive PMNS). " ++
  "Consistent with KamLAND-Zen < 36-156 meV. Within LEGEND-1000 reach (~10 meV)."
```
